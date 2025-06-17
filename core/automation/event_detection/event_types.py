"""
AADF Event Type Definitions
Defines all events that can trigger automated AI actions
"""

from dataclasses import dataclass
from typing import Dict, Any, Optional, List
from enum import Enum
from datetime import datetime


class EventType(Enum):
    """Core event types that trigger automation"""
    # Git events
    NEW_COMMIT = "new_commit"
    NEW_BRANCH = "new_branch"
    PR_CREATED = "pr_created"
    PR_MERGED = "pr_merged"
    
    # Time-based events
    SESSION_START = "session_start"
    SESSION_END = "session_end"
    DAILY_STANDUP = "daily_standup"
    WEEKLY_REVIEW = "weekly_review"
    
    # Development events
    BUILD_FAILURE = "build_failure"
    TEST_FAILURE = "test_failure"
    LINT_ERROR = "lint_error"
    TYPE_ERROR = "type_error"
    
    # Pattern events
    PATTERN_DISCOVERED = "pattern_discovered"
    PATTERN_APPLIED = "pattern_applied"
    ACCELERATION_MILESTONE = "acceleration_milestone"
    
    # Business events
    ISSUE_CREATED = "issue_created"
    REQUIREMENT_ADDED = "requirement_added"
    STAKEHOLDER_FEEDBACK = "stakeholder_feedback"


class Priority(Enum):
    """Event priority levels"""
    CRITICAL = "critical"  # Requires immediate action
    HIGH = "high"         # Process within 5 minutes
    MEDIUM = "medium"     # Process within 30 minutes
    LOW = "low"          # Process when convenient


@dataclass
class AutomationEvent:
    """Base event structure for all automation triggers"""
    event_id: str
    event_type: EventType
    timestamp: datetime
    source: str  # Which system detected this event
    priority: Priority
    data: Dict[str, Any]  # Event-specific data
    
    # Automation metadata
    requires_human_approval: bool = False
    estimated_complexity: Optional[float] = None
    suggested_agents: Optional[List[str]] = None
    related_patterns: Optional[List[str]] = None
    
    def to_dict(self) -> Dict[str, Any]:
        """Convert event to dictionary for A2A messaging"""
        return {
            "event_id": self.event_id,
            "event_type": self.event_type.value,
            "timestamp": self.timestamp.isoformat(),
            "source": self.source,
            "priority": self.priority.value,
            "data": self.data,
            "requires_human_approval": self.requires_human_approval,
            "estimated_complexity": self.estimated_complexity,
            "suggested_agents": self.suggested_agents,
            "related_patterns": self.related_patterns
        }


class GitEvent(AutomationEvent):
    """Git-specific event data"""
    def __init__(self, repository: str, branch: str, commit_hash: Optional[str] = None,
                 author: Optional[str] = None, files_changed: Optional[List[str]] = None,
                 diff_stats: Optional[Dict[str, int]] = None, **kwargs):
        super().__init__(**kwargs)
        self.repository = repository
        self.branch = branch
        self.commit_hash = commit_hash
        self.author = author
        self.files_changed = files_changed
        self.diff_stats = diff_stats


class BuildEvent(AutomationEvent):
    """Build/CI-specific event data"""
    def __init__(self, build_id: str, build_url: str, error_message: Optional[str] = None,
                 failed_tests: Optional[List[str]] = None, log_excerpt: Optional[str] = None, **kwargs):
        super().__init__(**kwargs)
        self.build_id = build_id
        self.build_url = build_url
        self.error_message = error_message
        self.failed_tests = failed_tests
        self.log_excerpt = log_excerpt


class PatternEvent(AutomationEvent):
    """Pattern-related event data"""
    def __init__(self, pattern_name: str, pattern_category: str, acceleration_factor: float,
                 confidence_score: float, application_context: Optional[Dict[str, Any]] = None, **kwargs):
        super().__init__(**kwargs)
        self.pattern_name = pattern_name
        self.pattern_category = pattern_category
        self.acceleration_factor = acceleration_factor
        self.confidence_score = confidence_score
        self.application_context = application_context


# Event handlers mapping
EVENT_HANDLERS = {
    EventType.NEW_COMMIT: {
        "handler": "handle_new_commit",
        "priority": Priority.HIGH,
        "agents": ["framework-architect", "cto"],
        "patterns": ["pattern-extraction", "code-review"]
    },
    EventType.SESSION_START: {
        "handler": "handle_session_start",
        "priority": Priority.HIGH,
        "agents": ["cto", "strategic-advisor"],
        "patterns": ["session-planning", "task-prioritization"]
    },
    EventType.BUILD_FAILURE: {
        "handler": "handle_build_failure",
        "priority": Priority.CRITICAL,
        "agents": ["cto"],
        "patterns": ["error-diagnosis", "quick-fix"]
    },
    EventType.PATTERN_DISCOVERED: {
        "handler": "handle_pattern_discovered",
        "priority": Priority.MEDIUM,
        "agents": ["framework-architect"],
        "patterns": ["pattern-documentation", "pattern-validation"]
    }
}


def create_event(event_type: EventType, data: Dict[str, Any], 
                source: str = "automation-system") -> AutomationEvent:
    """Factory function to create appropriate event instances"""
    import uuid
    
    base_params = {
        "event_id": str(uuid.uuid4()),
        "event_type": event_type,
        "timestamp": datetime.now(),
        "source": source,
        "priority": EVENT_HANDLERS.get(event_type, {}).get("priority", Priority.MEDIUM),
        "data": data
    }
    
    # Set suggested agents and patterns from handlers
    if event_type in EVENT_HANDLERS:
        handler_config = EVENT_HANDLERS[event_type]
        base_params["suggested_agents"] = handler_config.get("agents", [])
        base_params["related_patterns"] = handler_config.get("patterns", [])
    
    # Create specific event types
    if event_type in [EventType.NEW_COMMIT, EventType.NEW_BRANCH, 
                     EventType.PR_CREATED, EventType.PR_MERGED]:
        # Extract git-specific fields from data
        git_params = {
            'repository': data.get('repository', ''),
            'branch': data.get('branch', ''),
            'commit_hash': data.get('commit_hash'),
            'author': data.get('author'),
            'files_changed': data.get('files_changed'),
            'diff_stats': data.get('diff_stats')
        }
        return GitEvent(**git_params, **base_params)
    elif event_type in [EventType.BUILD_FAILURE, EventType.TEST_FAILURE]:
        # Extract build-specific fields from data
        build_params = {
            'build_id': data.get('build_id', ''),
            'build_url': data.get('build_url', ''),
            'error_message': data.get('error_message'),
            'failed_tests': data.get('failed_tests'),
            'log_excerpt': data.get('log_excerpt')
        }
        return BuildEvent(**build_params, **base_params)
    elif event_type in [EventType.PATTERN_DISCOVERED, EventType.PATTERN_APPLIED]:
        # Extract pattern-specific fields from data
        pattern_params = {
            'pattern_name': data.get('pattern_name', ''),
            'pattern_category': data.get('pattern_category', ''),
            'acceleration_factor': data.get('acceleration_factor', 0.0),
            'confidence_score': data.get('confidence_score', 0.0),
            'application_context': data.get('application_context')
        }
        return PatternEvent(**pattern_params, **base_params)
    else:
        return AutomationEvent(**base_params)