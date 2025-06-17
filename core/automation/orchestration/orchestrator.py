#!/usr/bin/env python3
"""
AADF Autonomous Orchestrator
Converts events to tasks and routes them to appropriate AI agents
"""

import os
import sys
import json
import time
import asyncio
import subprocess
from datetime import datetime
from pathlib import Path
from typing import Dict, List, Optional, Any

# Add parent directory to path
sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

from event_detection.event_types import EventType, AutomationEvent, Priority


class TaskOrchestrator:
    """Central orchestration engine for autonomous AI coordination"""
    
    def __init__(self, repo_path: str = "."):
        self.repo_path = Path(repo_path).resolve()
        self.running = False
        self.event_queue = []
        self.active_tasks = {}
        self.automation_metrics = {
            "events_processed": 0,
            "tasks_created": 0,
            "tasks_completed": 0,
            "automation_rate": 0.0,
            "average_response_time": 0.0
        }
        
        # Event handlers
        self.event_handlers = {
            EventType.NEW_COMMIT: self.handle_new_commit,
            EventType.NEW_BRANCH: self.handle_new_branch,
            EventType.BUILD_FAILURE: self.handle_build_failure,
            EventType.SESSION_START: self.handle_session_start,
            EventType.PATTERN_DISCOVERED: self.handle_pattern_discovered
        }
        
        print("🤖 AADF Orchestrator initialized")
    
    async def autonomous_loop(self):
        """Main autonomous processing loop"""
        self.running = True
        print("🚀 Starting autonomous orchestration loop")
        
        while self.running:
            try:
                # Check for new events
                new_events = await self.check_for_events()
                
                # Process each event
                for event in new_events:
                    await self.process_event(event)
                
                # Update metrics
                self.update_metrics()
                
                # Brief pause
                await asyncio.sleep(5)
                
            except Exception as e:
                print(f"❌ Error in orchestration loop: {e}")
                await asyncio.sleep(10)
    
    async def check_for_events(self) -> List[Dict]:
        """Check for new events from various sources"""
        events = []
        
        # Check for event files from git-watcher
        event_dir = Path("/tmp")
        for event_file in event_dir.glob("aadf-event-*.json"):
            try:
                with open(event_file, "r") as f:
                    event_data = json.load(f)
                events.append(event_data)
                
                # Remove processed file
                event_file.unlink()
                
            except Exception as e:
                print(f"Error reading event file {event_file}: {e}")
        
        return events
    
    async def process_event(self, event_data: Dict):
        """Process a single event and route to appropriate handler"""
        start_time = time.time()
        
        print(f"\n📥 Processing event: {event_data['event_type']}")
        print(f"   Event ID: {event_data['event_id']}")
        print(f"   Priority: {event_data['priority']}")
        
        # Get event type
        try:
            event_type = EventType(event_data['event_type'])
        except ValueError:
            print(f"❌ Unknown event type: {event_data['event_type']}")
            return
        
        # Route to appropriate handler
        handler = self.event_handlers.get(event_type)
        if handler:
            await handler(event_data)
            self.automation_metrics["events_processed"] += 1
        else:
            print(f"⚠️  No handler for event type: {event_type.value}")
        
        # Update response time metric
        response_time = time.time() - start_time
        self.update_response_time(response_time)
        
        print(f"✅ Event processed in {response_time:.2f}s")
    
    async def handle_new_commit(self, event_data: Dict):
        """Handle new commit events"""
        print("🔍 Analyzing new commit...")
        
        # Extract commit details
        commit_hash = event_data['data'].get('commit_hash', '')[:8]
        files_changed = event_data['data'].get('files_changed', [])
        author = event_data['data'].get('author', 'Unknown')
        
        # Create tasks based on commit analysis
        tasks = []
        
        # Task 1: Extract patterns from commit
        if len(files_changed) > 0:
            tasks.append({
                "type": "PATTERN_EXTRACTION",
                "agent": "framework-architect",
                "priority": "HIGH",
                "description": f"Extract patterns from commit {commit_hash}",
                "data": {
                    "commit_hash": commit_hash,
                    "files": files_changed
                }
            })
        
        # Task 2: Code review if significant changes
        if event_data.get('estimated_complexity', 0) > 30:
            tasks.append({
                "type": "CODE_REVIEW",
                "agent": "cto",
                "priority": "HIGH",
                "description": f"Review commit {commit_hash} by {author}",
                "data": {
                    "commit_hash": commit_hash,
                    "complexity": event_data.get('estimated_complexity', 0)
                }
            })
        
        # Task 3: Update documentation if .md files changed
        md_files = [f for f in files_changed if f.endswith('.md')]
        if md_files:
            tasks.append({
                "type": "DOC_UPDATE",
                "agent": "framework-architect",
                "priority": "MEDIUM",
                "description": "Update documentation index",
                "data": {
                    "files": md_files
                }
            })
        
        # Execute tasks
        for task in tasks:
            await self.execute_task(task)
    
    async def handle_new_branch(self, event_data: Dict):
        """Handle new branch events"""
        branch_name = event_data['data'].get('branch', '')
        print(f"🌿 Setting up new branch: {branch_name}")
        
        # Create session setup task
        task = {
            "type": "BRANCH_SETUP",
            "agent": "cto",
            "priority": "MEDIUM",
            "description": f"Setup development environment for branch {branch_name}",
            "data": {
                "branch": branch_name
            }
        }
        
        await self.execute_task(task)
    
    async def handle_build_failure(self, event_data: Dict):
        """Handle build failure events"""
        print("🚨 Build failure detected - initiating emergency response")
        
        # High priority diagnostic task
        task = {
            "type": "BUILD_DIAGNOSIS",
            "agent": "cto",
            "priority": "CRITICAL",
            "description": "Diagnose and fix build failure",
            "data": event_data['data']
        }
        
        await self.execute_task(task)
    
    async def handle_session_start(self, event_data: Dict):
        """Handle session start events"""
        print("🏁 Starting autonomous development session")
        
        # Create session planning task
        task = {
            "type": "SESSION_PLANNING",
            "agent": "strategic-advisor",
            "priority": "HIGH",
            "description": "Plan objectives for development session",
            "data": {
                "session_duration": 90,
                "available_agents": ["cto", "framework-architect"]
            }
        }
        
        await self.execute_task(task)
    
    async def handle_pattern_discovered(self, event_data: Dict):
        """Handle pattern discovery events"""
        pattern_name = event_data['data'].get('pattern_name', '')
        print(f"💡 New pattern discovered: {pattern_name}")
        
        # Document pattern task
        task = {
            "type": "PATTERN_DOCUMENTATION",
            "agent": "framework-architect",
            "priority": "MEDIUM",
            "description": f"Document and validate pattern: {pattern_name}",
            "data": event_data['data']
        }
        
        await self.execute_task(task)
    
    async def execute_task(self, task: Dict):
        """Execute a task by sending to appropriate AI agent"""
        self.automation_metrics["tasks_created"] += 1
        
        print(f"\n🤖 Executing task: {task['description']}")
        print(f"   Type: {task['type']}")
        print(f"   Agent: {task['agent']}")
        print(f"   Priority: {task['priority']}")
        
        # For now, simulate task execution via A2A
        # In production, this would use actual A2A messaging
        
        try:
            # Construct A2A command
            subject = task['description']
            content = json.dumps(task['data'], indent=2)
            
            # Log the command we would execute
            a2a_command = [
                "./scripts/a2a-v5",
                "send",
                "automation-orchestrator",
                task['agent'],
                "REQUEST",
                task['priority'],
                subject,
                content
            ]
            
            print(f"   A2A Command: {' '.join(a2a_command[:7])}...")
            
            # In real implementation, we would execute:
            # subprocess.run(a2a_command, cwd=self.repo_path)
            
            # For demo, just mark as completed
            self.automation_metrics["tasks_completed"] += 1
            print(f"   ✅ Task queued for {task['agent']}")
            
        except Exception as e:
            print(f"   ❌ Failed to execute task: {e}")
    
    def update_metrics(self):
        """Update automation metrics"""
        if self.automation_metrics["tasks_created"] > 0:
            self.automation_metrics["automation_rate"] = (
                self.automation_metrics["tasks_completed"] / 
                self.automation_metrics["tasks_created"] * 100
            )
    
    def update_response_time(self, response_time: float):
        """Update average response time metric"""
        current_avg = self.automation_metrics["average_response_time"]
        count = self.automation_metrics["events_processed"]
        
        # Calculate new average
        if count > 0:
            new_avg = (current_avg * (count - 1) + response_time) / count
            self.automation_metrics["average_response_time"] = new_avg
    
    def print_metrics(self):
        """Print current automation metrics"""
        print("\n📊 Automation Metrics:")
        print(f"   Events Processed: {self.automation_metrics['events_processed']}")
        print(f"   Tasks Created: {self.automation_metrics['tasks_created']}")
        print(f"   Tasks Completed: {self.automation_metrics['tasks_completed']}")
        print(f"   Automation Rate: {self.automation_metrics['automation_rate']:.1f}%")
        print(f"   Avg Response Time: {self.automation_metrics['average_response_time']:.2f}s")
    
    async def stop(self):
        """Stop the orchestrator"""
        self.running = False
        print("\n🛑 Orchestrator stopped")
        self.print_metrics()


async def main():
    """Main entry point"""
    import argparse
    
    parser = argparse.ArgumentParser(description="AADF Autonomous Orchestrator")
    parser.add_argument(
        "--repo",
        default=".",
        help="Path to repository (default: current directory)"
    )
    
    args = parser.parse_args()
    
    # Create orchestrator
    orchestrator = TaskOrchestrator(args.repo)
    
    try:
        # Start autonomous loop
        await orchestrator.autonomous_loop()
    except KeyboardInterrupt:
        print("\n\nShutting down...")
        await orchestrator.stop()


if __name__ == "__main__":
    asyncio.run(main())