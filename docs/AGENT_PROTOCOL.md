# AADF Agent Coordination Protocol

## Overview
This protocol defines how AI agents work together in any AADF project.

## Agent Roles and Responsibilities

### 1. AI-CTO (Technical Lead)
- **Primary**: Architecture, technical decisions, code quality
- **Coordinates**: All other agents
- **Reports to**: Human CEO/Founder
- **A2A Priority**: Reviews all HIGH priority messages

### 2. AI-Frontend
- **Primary**: UI components, user experience, accessibility
- **Coordinates with**: AI-CTO, AI-QA
- **Reports to**: AI-CTO
- **A2A Focus**: UI bugs, component requests, UX improvements

### 3. AI-Backend
- **Primary**: APIs, databases, business logic
- **Coordinates with**: AI-CTO, AI-Frontend, AI-DevOps
- **Reports to**: AI-CTO
- **A2A Focus**: API design, performance, data integrity

### 4. AI-QA
- **Primary**: Testing strategy, bug discovery, quality metrics
- **Coordinates with**: All agents
- **Reports to**: AI-CTO
- **A2A Focus**: Bug reports, test failures, coverage gaps

### 5. AI-DevOps
- **Primary**: Infrastructure, CI/CD, monitoring
- **Coordinates with**: AI-CTO, AI-Backend
- **Reports to**: AI-CTO
- **A2A Focus**: Deployments, infrastructure issues, performance

### 6. AI-Junior
- **Primary**: Learning tasks, documentation, simple features
- **Coordinates with**: Assigned mentor (any senior agent)
- **Reports to**: Mentor
- **A2A Focus**: Questions, completed tasks, learning progress

## Communication Patterns

### 1. Daily Sync Pattern
```bash
# Start of day (each agent)
./scripts/a2a-v5 send $AGENT_NAME ai-cto UPDATE MEDIUM "Daily Status" "
- Yesterday: [completed tasks]
- Today: [planned work]
- Blockers: [any issues]
"
```

### 2. Task Assignment Pattern
```bash
# CTO assigns task
./scripts/a2a-v5 send ai-cto ai-frontend REQUEST HIGH "Implement User Dashboard" "
Priority: HIGH
Deadline: Session 5
Requirements:
- Real-time data updates
- Mobile responsive
- Accessibility compliant
"

# Frontend acknowledges
./scripts/a2a-v5 send ai-frontend ai-cto UPDATE HIGH "Re: User Dashboard" "
Task acknowledged. 
Estimated sessions: 3
Starting: Session 2
"
```

### 3. Bug Report Pattern
```bash
# QA reports bug
./scripts/a2a-v5 send ai-qa ai-backend REQUEST HIGH "Critical: API returning 500" "
Endpoint: /api/users
Method: POST
Reproduction: [steps]
Expected: 201 Created
Actual: 500 Error
"

# Backend responds
./scripts/a2a-v5 send ai-backend ai-qa UPDATE HIGH "Re: API 500 Error" "
Bug confirmed and fixed.
Cause: Missing validation
Fix: Commit abc123
Please retest.
"
```

### 4. Convergent Validation Pattern
```bash
# CTO proposes pattern
./scripts/a2a-v5 send ai-cto all REQUEST MEDIUM "Pattern Validation: Optimistic UI" "
Discovered pattern: Optimistic UI updates
Implementation: [details]
Impact: 300ms faster perceived performance
Please validate in your domain.
"

# Multiple agents validate
./scripts/a2a-v5 send ai-frontend ai-cto FEEDBACK MEDIUM "Re: Optimistic UI Pattern" "
Validated in checkout flow.
Results: 280ms improvement
Recommendation: Adopt project-wide
"
```

## Session Coordination

### 1. Non-Overlapping Sessions
- Agents work in different time blocks to avoid conflicts
- Example schedule:
  - AI-CTO: Morning (9-12)
  - AI-Frontend: Early afternoon (12-3)
  - AI-Backend: Late afternoon (3-6)
  - AI-QA: Evening (6-8)

### 2. Handoff Protocol
```bash
# End of session handoff
./scripts/a2a-v5 send ai-frontend ai-backend UPDATE HIGH "Session 3 Complete" "
Completed:
- User profile UI
- API integration started

Handoff:
- Need GET /api/user/:id endpoint
- Response format in types/user.ts

Branch: session/ai-frontend/2024-01-13-3
"
```

### 3. Emergency Escalation
```bash
# Critical issue escalation
./scripts/a2a-v5 send ai-qa ai-cto REQUEST HIGH "CRITICAL: Production Down" "
URGENT: Main API unresponsive
Started: 14:30 UTC
Impact: All users
Logs: [error details]
"
```

## State Management

### 1. Agent State Files
Each agent maintains state in `.ai/agents/[agent-name]/state.json`:
```json
{
  "agent": "ai-frontend",
  "status": "active",
  "current_task": "user-dashboard",
  "session_number": 3,
  "branch": "session/ai-frontend/2024-01-13-3",
  "blockers": [],
  "patterns_discovered": ["optimistic-ui", "skeleton-loading"]
}
```

### 2. Shared Context
Project-wide context in `.ai/project-state.json`:
```json
{
  "sprint": 1,
  "phase": "mvp",
  "active_features": ["auth", "dashboard"],
  "blocked_features": [],
  "team_velocity": 8.5
}
```

## Metrics and Reporting

### 1. Individual Metrics
Each agent tracks:
- Sessions completed
- Tasks finished
- Patterns discovered
- Bugs found/fixed
- Code contributed

### 2. Team Metrics
AI-CTO aggregates:
- Overall velocity
- Team acceleration
- Pattern adoption
- Quality metrics
- Sprint progress

### 3. Weekly Report Pattern
```bash
# CTO sends weekly summary
./scripts/a2a-v5 send ai-cto human-ceo REPORT HIGH "Week 1 Summary" "
Team Performance:
- Velocity: 8.5x (target: 10x)
- Features completed: 3/5
- Patterns discovered: 7
- Test coverage: 82%

Next Week:
- Complete MVP features
- Performance optimization
- Deployment preparation
"
```

## Best Practices

### DO
- ✅ Acknowledge all HIGH priority messages within 1 session
- ✅ Update state files at session end
- ✅ Use clear, specific subjects
- ✅ Include reproduction steps for bugs
- ✅ Validate patterns before adoption

### DON'T
- ❌ Work on same files simultaneously
- ❌ Skip session handoffs
- ❌ Ignore A2A messages
- ❌ Make architectural changes without CTO approval
- ❌ Deploy without DevOps coordination

## Example Multi-Agent Flow

1. **Human CEO** → AI-CTO: "Build user authentication"
2. **AI-CTO** → Team: Breaks down into tasks
3. **AI-Backend**: Implements auth API
4. **AI-Frontend**: Creates login UI
5. **AI-QA**: Writes auth tests
6. **AI-DevOps**: Sets up auth infrastructure
7. **AI-Junior**: Documents auth flow
8. **AI-CTO** → Human CEO: "Auth complete, tested, deployed"

This protocol ensures smooth coordination regardless of project type or team size.