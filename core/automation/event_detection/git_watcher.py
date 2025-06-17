#!/usr/bin/env python3
"""
Git Event Watcher
Monitors git repository for events that trigger automated AI actions
"""

import os
import sys
import time
import json
import subprocess
from datetime import datetime
from typing import Dict, List, Optional, Set
from pathlib import Path

# Add parent directory to path for imports
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

from event_types import EventType, create_event, Priority


class GitWatcher:
    """Monitors git repository for automation-triggering events"""
    
    def __init__(self, repo_path: str = ".", poll_interval: int = 10):
        self.repo_path = Path(repo_path).resolve()
        self.poll_interval = poll_interval
        self.last_commit_hash = None
        self.known_branches: Set[str] = set()
        self.running = False
        
        # Event queue for processing
        self.event_queue = []
        
        # Initialize state
        self._initialize_state()
    
    def _initialize_state(self):
        """Initialize watcher state from current git status"""
        try:
            # Get current commit
            self.last_commit_hash = self._get_current_commit()
            
            # Get all branches
            branches = self._get_all_branches()
            self.known_branches = set(branches)
            
            print(f"Git Watcher initialized:")
            print(f"  Repository: {self.repo_path}")
            print(f"  Current commit: {self.last_commit_hash[:8]}")
            print(f"  Known branches: {len(self.known_branches)}")
            
        except Exception as e:
            print(f"Error initializing git watcher: {e}")
            raise
    
    def _run_git_command(self, command: List[str]) -> str:
        """Run a git command and return output"""
        try:
            result = subprocess.run(
                ["git"] + command,
                cwd=self.repo_path,
                capture_output=True,
                text=True,
                check=True
            )
            return result.stdout.strip()
        except subprocess.CalledProcessError as e:
            print(f"Git command failed: {e}")
            return ""
    
    def _get_current_commit(self) -> str:
        """Get the current HEAD commit hash"""
        return self._run_git_command(["rev-parse", "HEAD"])
    
    def _get_all_branches(self) -> List[str]:
        """Get all branch names"""
        output = self._run_git_command(["branch", "-a"])
        branches = []
        for line in output.split("\n"):
            branch = line.strip().lstrip("* ")
            if branch:
                branches.append(branch)
        return branches
    
    def _get_commit_info(self, commit_hash: str) -> Dict[str, any]:
        """Get detailed information about a commit"""
        # Get commit details
        format_str = "%H|%an|%ae|%s|%b"
        output = self._run_git_command(["show", "-s", f"--format={format_str}", commit_hash])
        
        if not output:
            return {}
        
        parts = output.split("|", 4)
        if len(parts) < 4:
            return {}
        
        # Get changed files
        files_output = self._run_git_command(["diff-tree", "--no-commit-id", "--name-only", "-r", commit_hash])
        files_changed = files_output.split("\n") if files_output else []
        
        # Get diff stats
        stats_output = self._run_git_command(["diff-tree", "--no-commit-id", "--numstat", "-r", commit_hash])
        
        return {
            "commit_hash": parts[0],
            "author": parts[1],
            "author_email": parts[2],
            "subject": parts[3],
            "body": parts[4] if len(parts) > 4 else "",
            "files_changed": files_changed,
            "diff_stats": self._parse_diff_stats(stats_output)
        }
    
    def _parse_diff_stats(self, stats_output: str) -> Dict[str, Dict[str, int]]:
        """Parse git diff numstat output"""
        stats = {}
        for line in stats_output.split("\n"):
            if line:
                parts = line.split("\t")
                if len(parts) == 3:
                    stats[parts[2]] = {
                        "additions": int(parts[0]) if parts[0] != "-" else 0,
                        "deletions": int(parts[1]) if parts[1] != "-" else 0
                    }
        return stats
    
    def _check_for_new_commits(self):
        """Check for new commits and generate events"""
        current_commit = self._get_current_commit()
        
        if current_commit != self.last_commit_hash:
            # Get all commits between last known and current
            if self.last_commit_hash:
                commit_range = f"{self.last_commit_hash}..{current_commit}"
                new_commits = self._run_git_command(["rev-list", commit_range])
                
                for commit_hash in new_commits.split("\n"):
                    if commit_hash:
                        self._handle_new_commit(commit_hash)
            else:
                # First run, just track current commit
                self._handle_new_commit(current_commit)
            
            self.last_commit_hash = current_commit
    
    def _handle_new_commit(self, commit_hash: str):
        """Process a new commit and create event"""
        commit_info = self._get_commit_info(commit_hash)
        
        if not commit_info:
            return
        
        # Determine priority based on commit characteristics
        priority = self._determine_commit_priority(commit_info)
        
        # Check for patterns in commit
        patterns = self._detect_patterns_in_commit(commit_info)
        
        # Create event
        event_data = {
            "repository": str(self.repo_path),
            "branch": self._run_git_command(["rev-parse", "--abbrev-ref", "HEAD"]),
            "commit_hash": commit_hash,
            "author": commit_info["author"],
            "files_changed": commit_info["files_changed"],
            "diff_stats": commit_info["diff_stats"]
        }
        
        event = create_event(
            EventType.NEW_COMMIT,
            event_data,
            source="git-watcher"
        )
        
        # Override priority if needed
        event.priority = priority
        
        # Add pattern suggestions
        if patterns:
            event.related_patterns = patterns
        
        # Estimate complexity based on changes
        event.estimated_complexity = self._estimate_commit_complexity(commit_info)
        
        self.event_queue.append(event)
        print(f"\n🔍 New commit detected: {commit_hash[:8]}")
        print(f"   Author: {commit_info['author']}")
        print(f"   Files changed: {len(commit_info['files_changed'])}")
        print(f"   Priority: {priority.value}")
        print(f"   Complexity: {event.estimated_complexity:.2f}")
    
    def _determine_commit_priority(self, commit_info: Dict) -> Priority:
        """Determine priority based on commit characteristics"""
        subject = commit_info["subject"].lower()
        
        # Critical keywords
        if any(keyword in subject for keyword in ["fix", "bug", "critical", "urgent"]):
            return Priority.CRITICAL
        
        # High priority keywords
        if any(keyword in subject for keyword in ["feat", "feature", "refactor"]):
            return Priority.HIGH
        
        # Check file count
        if len(commit_info["files_changed"]) > 10:
            return Priority.HIGH
        
        return Priority.MEDIUM
    
    def _detect_patterns_in_commit(self, commit_info: Dict) -> List[str]:
        """Detect which patterns might apply to this commit"""
        patterns = []
        
        # Check for test files
        if any("test" in f for f in commit_info["files_changed"]):
            patterns.append("test-pattern")
        
        # Check for documentation
        if any(f.endswith(".md") for f in commit_info["files_changed"]):
            patterns.append("documentation-pattern")
        
        # Check for refactoring
        if "refactor" in commit_info["subject"].lower():
            patterns.append("refactoring-pattern")
        
        # Check for new features
        if any(word in commit_info["subject"].lower() for word in ["feat", "feature", "add"]):
            patterns.append("feature-pattern")
        
        return patterns
    
    def _estimate_commit_complexity(self, commit_info: Dict) -> float:
        """Estimate complexity score (0-100) based on commit characteristics"""
        complexity = 0.0
        
        # File count factor
        file_count = len(commit_info["files_changed"])
        complexity += min(file_count * 2, 30)  # Max 30 points for files
        
        # Lines changed factor
        total_changes = 0
        for stats in commit_info["diff_stats"].values():
            total_changes += stats["additions"] + stats["deletions"]
        complexity += min(total_changes / 10, 30)  # Max 30 points for lines
        
        # File type diversity
        extensions = set()
        for file in commit_info["files_changed"]:
            if "." in file:
                extensions.add(file.split(".")[-1])
        complexity += min(len(extensions) * 5, 20)  # Max 20 points for diversity
        
        # Integration complexity (multiple directories)
        directories = set()
        for file in commit_info["files_changed"]:
            directories.add(os.path.dirname(file))
        complexity += min(len(directories) * 3, 20)  # Max 20 points for integration
        
        return min(complexity, 100)
    
    def _check_for_new_branches(self):
        """Check for new branches and generate events"""
        current_branches = set(self._get_all_branches())
        new_branches = current_branches - self.known_branches
        
        for branch in new_branches:
            self._handle_new_branch(branch)
        
        self.known_branches = current_branches
    
    def _handle_new_branch(self, branch_name: str):
        """Process a new branch and create event"""
        event_data = {
            "repository": str(self.repo_path),
            "branch": branch_name,
            "created_from": self._run_git_command(["rev-parse", "--abbrev-ref", "HEAD"])
        }
        
        event = create_event(
            EventType.NEW_BRANCH,
            event_data,
            source="git-watcher"
        )
        
        self.event_queue.append(event)
        print(f"\n🌿 New branch detected: {branch_name}")
    
    def process_events(self):
        """Process queued events (send to orchestrator)"""
        while self.event_queue:
            event = self.event_queue.pop(0)
            
            # For now, just log the event
            # TODO: Send to orchestrator via A2A
            print(f"\n📤 Processing event: {event.event_type.value}")
            print(f"   Event ID: {event.event_id}")
            print(f"   Data: {json.dumps(event.data, indent=2)}")
            
            # Write event to file for orchestrator to pick up
            event_file = Path(f"/tmp/aadf-event-{event.event_id}.json")
            with open(event_file, "w") as f:
                json.dump(event.to_dict(), f, indent=2)
            
            print(f"   Written to: {event_file}")
    
    def start(self):
        """Start monitoring for git events"""
        self.running = True
        print("\n🚀 Git Watcher started")
        print(f"   Polling interval: {self.poll_interval} seconds")
        print("   Press Ctrl+C to stop\n")
        
        try:
            while self.running:
                # Check for various git events
                self._check_for_new_commits()
                self._check_for_new_branches()
                
                # Process any queued events
                self.process_events()
                
                # Wait before next check
                time.sleep(self.poll_interval)
                
        except KeyboardInterrupt:
            print("\n\n🛑 Git Watcher stopped")
            self.running = False
    
    def stop(self):
        """Stop the watcher"""
        self.running = False


def main():
    """Main entry point"""
    import argparse
    
    parser = argparse.ArgumentParser(description="AADF Git Event Watcher")
    parser.add_argument(
        "--repo",
        default=".",
        help="Path to git repository to watch (default: current directory)"
    )
    parser.add_argument(
        "--interval",
        type=int,
        default=10,
        help="Polling interval in seconds (default: 10)"
    )
    
    args = parser.parse_args()
    
    # Create and start watcher
    watcher = GitWatcher(args.repo, args.interval)
    watcher.start()


if __name__ == "__main__":
    main()