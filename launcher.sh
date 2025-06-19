#!/bin/bash

# AADF Universal Project Launcher
# Works for ANY project type with customizable agent teams

set -e

# Colors
GREEN='\033[0;32m'
BLUE='\033[0;34m'
YELLOW='\033[1;33m'
CYAN='\033[0;36m'
RED='\033[0;31m'
NC='\033[0m'

# Banner
echo -e "${BLUE}╔═══════════════════════════════════════════════════════════════╗${NC}"
echo -e "${BLUE}║          AADF Universal Project Launcher v1.0.0               ║${NC}"
echo -e "${BLUE}║      Start ANY project at 10x with AI agent teams            ║${NC}"
echo -e "${BLUE}╚═══════════════════════════════════════════════════════════════╝${NC}"

# Project Configuration
PROJECT_NAME=""
PROJECT_DIR=""
PROJECT_TYPE=""
PRIMARY_LANGUAGE=""
AGENT_TEAM_SIZE=""
SELECTED_AGENTS=()
GITHUB_ORG=""

# Step 1: Project Basics
echo -e "\n${CYAN}Step 1: Project Basics${NC}"
read -p "Project name: " PROJECT_NAME
read -p "Project directory (default: ./$PROJECT_NAME): " PROJECT_DIR
PROJECT_DIR=${PROJECT_DIR:-./$PROJECT_NAME}
read -p "GitHub organization (optional): " GITHUB_ORG

# Step 2: Project Type
echo -e "\n${CYAN}Step 2: Project Type${NC}"
echo "1) Web Application (Next.js)"
echo "2) API Service (Node/Express)"
echo "3) CLI Tool"
echo "4) Mobile App (React Native)"
echo "5) Machine Learning Pipeline"
echo "6) Documentation Site"
echo "7) Custom"
read -p "Select project type [1-7]: " PROJECT_TYPE_CHOICE

case $PROJECT_TYPE_CHOICE in
    1) PROJECT_TYPE="web-app" ;;
    2) PROJECT_TYPE="api-service" ;;
    3) PROJECT_TYPE="cli-tool" ;;
    4) PROJECT_TYPE="mobile-app" ;;
    5) PROJECT_TYPE="ml-pipeline" ;;
    6) PROJECT_TYPE="docs-site" ;;
    7) PROJECT_TYPE="custom" ;;
    *) PROJECT_TYPE="web-app" ;;
esac

# Step 3: Primary Language
echo -e "\n${CYAN}Step 3: Primary Language${NC}"
echo "1) TypeScript (recommended)"
echo "2) JavaScript"
echo "3) Python"
echo "4) Go"
echo "5) Rust"
read -p "Select primary language [1-5]: " LANG_CHOICE

case $LANG_CHOICE in
    1) PRIMARY_LANGUAGE="typescript" ;;
    2) PRIMARY_LANGUAGE="javascript" ;;
    3) PRIMARY_LANGUAGE="python" ;;
    4) PRIMARY_LANGUAGE="go" ;;
    5) PRIMARY_LANGUAGE="rust" ;;
    *) PRIMARY_LANGUAGE="typescript" ;;
esac

# Step 4: Agent Team Composition
echo -e "\n${CYAN}Step 4: AI Agent Team${NC}"
echo "1) Solo (Just AI-CTO)"
echo "2) Small Team (CTO + 2 specialists)"
echo "3) Full Team (CTO + 4-5 specialists)"
echo "4) Custom Selection"
read -p "Select team size [1-4]: " TEAM_CHOICE

case $TEAM_CHOICE in
    1) 
        AGENT_TEAM_SIZE="solo"
        SELECTED_AGENTS=("ai-cto")
        ;;
    2) 
        AGENT_TEAM_SIZE="small"
        SELECTED_AGENTS=("ai-cto" "ai-frontend" "ai-qa")
        ;;
    3) 
        AGENT_TEAM_SIZE="full"
        SELECTED_AGENTS=("ai-cto" "ai-frontend" "ai-backend" "ai-qa" "ai-devops")
        ;;
    4) 
        AGENT_TEAM_SIZE="custom"
        echo "Available agents:"
        echo "  ai-cto      - Technical leadership"
        echo "  ai-frontend - UI/UX specialist"
        echo "  ai-backend  - API/Database specialist"
        echo "  ai-qa       - Testing specialist"
        echo "  ai-devops   - Infrastructure specialist"
        echo "  ai-junior   - Learning assistant"
        read -p "Enter agents (comma-separated): " CUSTOM_AGENTS
        IFS=',' read -ra SELECTED_AGENTS <<< "$CUSTOM_AGENTS"
        ;;
esac

# Step 5: Automation Setup
echo -e "\n${CYAN}Step 5: Event-Driven Automation${NC}"
echo "Enable autonomous development with event-driven automation?"
echo "This includes:"
echo "  • Git event detection (commits, PRs, issues)"
echo "  • Automatic task assignment to agents"
echo "  • Real-time orchestration"
echo "  • Activity dashboard"
echo ""
read -p "Enable automation? [Y/n]: " ENABLE_AUTOMATION
ENABLE_AUTOMATION=${ENABLE_AUTOMATION:-Y}

# Step 6: Confirmation
echo -e "\n${CYAN}Step 6: Configuration Summary${NC}"
echo -e "Project Name: ${GREEN}$PROJECT_NAME${NC}"
echo -e "Directory: ${GREEN}$PROJECT_DIR${NC}"
echo -e "Type: ${GREEN}$PROJECT_TYPE${NC}"
echo -e "Language: ${GREEN}$PRIMARY_LANGUAGE${NC}"
echo -e "Agents: ${GREEN}${SELECTED_AGENTS[*]}${NC}"
echo -e "GitHub Org: ${GREEN}${GITHUB_ORG:-none}${NC}"
echo -e "Automation: ${GREEN}$([ "$ENABLE_AUTOMATION" == "Y" ] || [ "$ENABLE_AUTOMATION" == "y" ] && echo "Enabled" || echo "Disabled")${NC}"
echo ""
read -p "Proceed with creation? [Y/n]: " CONFIRM
if [[ $CONFIRM == "n" || $CONFIRM == "N" ]]; then
    echo "Cancelled."
    exit 0
fi

# Create Project
echo -e "\n${BLUE}🚀 Creating AADF Project...${NC}"

# Create directory structure
mkdir -p "$PROJECT_DIR"
cd "$PROJECT_DIR"

# Initialize AADF structure
echo -e "${GREEN}📁 Creating AADF directories...${NC}"
mkdir -p {.ai/{agents,communication/{inbox,outbox,archive},patterns,coordination,metrics},scripts,docs}

# Create A2A v5 messaging script inline
echo -e "${GREEN}📬 Creating A2A v5 messaging...${NC}"
cat > scripts/a2a-v5 << 'EOFA2A'
#!/bin/bash
# A2A v5 - Agent to Agent Communication Protocol
# Simple file-based messaging for AI agents

COMM_DIR=".ai/communication"
COMMAND=$1

case $COMMAND in
    send)
        FROM=$2
        TO=$3
        TYPE=$4
        PRIORITY=$5
        SUBJECT=$6
        BODY=$7
        TIMESTAMP=$(date -u +"%Y-%m-%dT%H:%M:%SZ")
        ID=$(uuidgen 2>/dev/null || echo "${TIMESTAMP}-${RANDOM}")
        
        MESSAGE=$(cat <<EOF
{
  "id": "$ID",
  "from": "$FROM",
  "to": "$TO",
  "type": "$TYPE",
  "priority": "$PRIORITY",
  "subject": "$SUBJECT",
  "body": "$BODY",
  "timestamp": "$TIMESTAMP",
  "status": "unread"
}
EOF
)
        echo "$MESSAGE" > "$COMM_DIR/inbox/${TO}_${ID}.json"
        echo "✉️  Message sent: $FROM → $TO"
        ;;
    inbox)
        AGENT=${2:-$(basename $PWD)}
        echo "📥 Inbox for $AGENT:"
        ls -la $COMM_DIR/inbox/${AGENT}_*.json 2>/dev/null | wc -l | xargs echo "Messages:"
        ;;
    read)
        AGENT=${2:-$(basename $PWD)}
        for msg in $COMM_DIR/inbox/${AGENT}_*.json; do
            [ -f "$msg" ] && cat "$msg" && echo ""
        done
        ;;
    *)
        echo "Usage: a2a-v5 [send|inbox|read] [args...]"
        ;;
esac
EOFA2A
chmod +x scripts/a2a-v5

# Install automation if enabled
if [[ "$ENABLE_AUTOMATION" == "Y" ]] || [[ "$ENABLE_AUTOMATION" == "y" ]]; then
    echo -e "${GREEN}🤖 Installing automation framework...${NC}"
    
    # Create automation directories
    mkdir -p scripts/automation
    mkdir -p .ai/automation/{events,tasks,logs}
    
    # Create orchestrator config based on selected agents
    cat > scripts/automation/orchestrator-config.json << EOF
{
  "agents": $(printf '%s\n' "${SELECTED_AGENTS[@]}" | jq -R . | jq -s .),
  "event_handlers": {
    "commit_pushed": {
      "assignee": "ai-cto",
      "priority": "MEDIUM"
    },
    "pr_created": {
      "assignee": "ai-qa",
      "priority": "HIGH"
    },
    "issue_opened": {
      "assignee": "ai-cto",
      "priority": "HIGH"
    },
    "test_failed": {
      "assignee": "ai-qa",
      "priority": "HIGH"
    }
  },
  "automation_enabled": true,
  "dashboard_port": 8080
}
EOF
    
    # Copy automation source files
    AUTOMATION_SOURCE="$(dirname "$0")/core/automation"
    if [ -d "$AUTOMATION_SOURCE" ]; then
        echo "Copying automation framework files..."
        cp -r "$AUTOMATION_SOURCE/event_detection" scripts/automation/
        cp -r "$AUTOMATION_SOURCE/orchestration" scripts/automation/
        cp -r "$AUTOMATION_SOURCE/monitoring" scripts/automation/
        cp "$AUTOMATION_SOURCE"/*.sh scripts/automation/ 2>/dev/null || true
        cp "$AUTOMATION_SOURCE"/requirements.txt scripts/automation/
        chmod +x scripts/automation/*.sh 2>/dev/null || true
        
        # Create start script
        cat > scripts/automation/start-automation.sh << 'EOFAUTO'
#!/bin/bash
echo "🚀 Starting AADF Automation System"
echo "=================================="

# Start in project root
cd "$(dirname "$0")/../.."

# Start event watcher
echo "Starting git event watcher..."
python3 scripts/automation/event_detection/git_watcher.py > .ai/automation/logs/git-watcher.log 2>&1 &
echo $! > .ai/automation/logs/git-watcher.pid

# Start orchestrator
echo "Starting task orchestrator..."
python3 scripts/automation/orchestration/orchestrator.py > .ai/automation/logs/orchestrator.log 2>&1 &
echo $! > .ai/automation/logs/orchestrator.pid

echo "✅ Automation started!"
echo ""
echo "Monitor with: python3 scripts/automation/monitoring/dashboard.py"
echo "Stop with: ./scripts/automation/stop-automation.sh"
EOFAUTO
        chmod +x scripts/automation/start-automation.sh
        
        # Create stop script
        cat > scripts/automation/stop-automation.sh << 'EOFAUTO'
#!/bin/bash
echo "🛑 Stopping AADF Automation"

cd "$(dirname "$0")/../.."

# Stop processes
if [ -f .ai/automation/logs/git-watcher.pid ]; then
    kill $(cat .ai/automation/logs/git-watcher.pid) 2>/dev/null
    rm .ai/automation/logs/git-watcher.pid
fi

if [ -f .ai/automation/logs/orchestrator.pid ]; then
    kill $(cat .ai/automation/logs/orchestrator.pid) 2>/dev/null
    rm .ai/automation/logs/orchestrator.pid
fi

echo "✅ Automation stopped"
EOFAUTO
        chmod +x scripts/automation/stop-automation.sh
    else
        echo -e "${YELLOW}⚠️  Automation source not found. Creating basic scripts...${NC}"
        
        # Create placeholder scripts
        cat > scripts/automation/start-automation.sh << 'EOFAUTO'
#!/bin/bash
echo "⚠️  Automation framework not fully installed."
echo "Please install automation components manually."
EOFAUTO
        chmod +x scripts/automation/start-automation.sh
        
        cp scripts/automation/start-automation.sh scripts/automation/stop-automation.sh
    fi
    
    # Run automation starter to create scripts
    AUTOMATION_STARTER="$(dirname "$0")/project-template/automation-starter.sh"
    if [ -f "$AUTOMATION_STARTER" ]; then
        bash "$AUTOMATION_STARTER"
    else
        # Create minimal automation scripts inline
        echo "Creating automation scripts..."
        
        # Git watcher
        cat > scripts/automation/git-watcher.py << 'EOFPY'
#!/usr/bin/env python3
import os, json, time, subprocess
from datetime import datetime

def get_latest_commit():
    try:
        result = subprocess.run(['git', 'log', '-1', '--format=%H|%s'], capture_output=True, text=True)
        if result.returncode == 0:
            parts = result.stdout.strip().split('|')
            return {'hash': parts[0], 'message': parts[1]}
    except: pass
    return None

def create_task(event_type, data):
    task = {'id': f"{event_type}_{int(time.time())}", 'type': event_type, 'data': data, 'created': datetime.now().isoformat(), 'status': 'pending'}
    with open(f".ai/automation/tasks/{task['id']}.json", 'w') as f:
        json.dump(task, f, indent=2)
    os.system(f"./scripts/a2a-v5 send automation ai-cto REQUEST MEDIUM 'New {event_type}' '{data}'")
    print(f"✅ Created task: {task['id']}")

print("👀 Watching for git events...")
last_commit = get_latest_commit()
while True:
    current_commit = get_latest_commit()
    if current_commit and current_commit['hash'] != last_commit['hash']:
        print(f"🔔 New commit: {current_commit['message']}")
        create_task('commit_pushed', current_commit)
        last_commit = current_commit
    time.sleep(5)
EOFPY
        chmod +x scripts/automation/git-watcher.py
        
        # Start/stop scripts
        cat > scripts/automation/start-automation.sh << 'EOFSH'
#!/bin/bash
echo "🚀 Starting automation..."
nohup python3 scripts/automation/git-watcher.py > .ai/automation/logs/git-watcher.log 2>&1 &
echo $! > .ai/automation/git-watcher.pid
echo "✅ Automation started (PID: $(cat .ai/automation/git-watcher.pid))"
EOFSH
        chmod +x scripts/automation/start-automation.sh
        
        cat > scripts/automation/stop-automation.sh << 'EOFSH'
#!/bin/bash
if [ -f .ai/automation/git-watcher.pid ]; then
    kill $(cat .ai/automation/git-watcher.pid) 2>/dev/null
    rm .ai/automation/git-watcher.pid
fi
echo "✅ Automation stopped"
EOFSH
        chmod +x scripts/automation/stop-automation.sh
    fi
fi

# Set up agent configurations
echo -e "${GREEN}🤖 Configuring AI agents...${NC}"
for agent in "${SELECTED_AGENTS[@]}"; do
    agent=$(echo "$agent" | xargs) # Trim whitespace
    
    # Create agent directory
    mkdir -p ".ai/agents/$agent"
    
    # Copy agent template if exists
    AGENT_TEMPLATE="$(dirname "$0")/core/agents/$agent.json"
    if [ -f "$AGENT_TEMPLATE" ]; then
        cp "$AGENT_TEMPLATE" ".ai/agents/$agent/config.json"
    else
        # Create basic agent config
        cat > ".ai/agents/$agent/config.json" << EOF
{
  "role": "$agent",
  "name": "AI Agent - $agent",
  "active": true,
  "session_count": 0,
  "current_focus": "project initialization"
}
EOF
    fi
    
    # Create inbox/outbox for agent
    mkdir -p ".ai/communication/inbox/$agent"
    mkdir -p ".ai/communication/outbox/$agent"
    
    # Create state file
    cat > ".ai/agents/$agent/state.json" << EOF
{
  "agent": "$agent",
  "status": "active",
  "last_session": null,
  "total_sessions": 0,
  "patterns_discovered": 0,
  "current_task": null
}
EOF
done

# Create project-specific configuration
echo -e "${GREEN}⚙️  Creating project configuration...${NC}"
cat > .ai/project.json << EOF
{
  "name": "$PROJECT_NAME",
  "type": "$PROJECT_TYPE",
  "language": "$PRIMARY_LANGUAGE",
  "created": "$(date -u +%Y-%m-%dT%H:%M:%SZ)",
  "aadf_version": "1.0.0",
  "agents": $(printf '%s\n' "${SELECTED_AGENTS[@]}" | jq -R . | jq -s .),
  "metrics": {
    "baseline_velocity": 1,
    "target_acceleration": 48,
    "current_acceleration": 10
  }
}
EOF

# Create universal CLAUDE.md
cat > CLAUDE.md << EOF
# $PROJECT_NAME - AADF Project

## Project Configuration
- **Type**: $PROJECT_TYPE
- **Language**: $PRIMARY_LANGUAGE
- **Agents**: ${SELECTED_AGENTS[*]}
- **Target**: 48x acceleration

## Active AI Agents
$(for agent in "${SELECTED_AGENTS[@]}"; do
    echo "- **$agent**: See .ai/agents/$agent/config.json"
done)

## Commands
- \`./scripts/a2a-v5\` - Agent communication
- \`./scripts/session-manager.sh <agent> <number>\` - Start session
- \`./scripts/metrics-dashboard.sh\` - View metrics$(if [[ "$ENABLE_AUTOMATION" == "Y" ]] || [[ "$ENABLE_AUTOMATION" == "y" ]]; then echo "
- \`./scripts/automation/start-automation.sh\` - Start autonomous mode
- \`./scripts/automation/stop-automation.sh\` - Stop automation
- \`python3 scripts/automation/monitoring/dashboard.py\` - View real-time activity"; fi)

## Workflow Rules
1. **Sessions**: 60-90 minute focused work
2. **Commits**: Every 20-30 minutes with semantic prefixes
3. **Patterns**: Extract after each implementation
4. **A2A**: Use for all agent coordination
5. **Types**: No 'any' types (if using TypeScript)

## Agent Communication Protocol
- Messages via A2A v5 (main branch routing)
- Priority levels: HIGH, MEDIUM, LOW
- Types: REQUEST, UPDATE, DECISION, FEEDBACK

## Git Workflow
- Main branch for stable code
- Session branches: session/<agent>/<date>-<number>
- Feature branches: feature/<description>
- Always pull before starting session

## Metrics Tracking
- Commits per session
- Lines of code
- Pattern discoveries
- Test coverage
- Acceleration vs baseline

## Recovery Protocol
All agent state is in .ai/agents/<agent>/
Recovery: \`git checkout <branch>\` restores everything
$(if [[ "$ENABLE_AUTOMATION" == "Y" ]] || [[ "$ENABLE_AUTOMATION" == "y" ]]; then echo "
## Automation Mode

This project has event-driven automation enabled!

### How it works:
1. Git events (commits, PRs, issues) are detected automatically
2. Events create tasks assigned to appropriate agents
3. Agents work autonomously on assigned tasks
4. Monitor progress via dashboard

### Starting automation:
\`\`\`bash
# Start automation in background
./scripts/automation/start-automation.sh

# View real-time activity
python3 scripts/automation/monitoring/dashboard.py

# Stop automation
./scripts/automation/stop-automation.sh
\`\`\`

### Event → Agent Mapping:
- Commits pushed → ai-cto (code review)
- PRs created → ai-qa (testing)
- Issues opened → ai-cto (triage)
- Tests failed → ai-qa (debugging)"; fi)
EOF

# Create session manager for any agent
cat > scripts/session-manager.sh << 'EOF'
#!/bin/bash
# AADF Universal Session Manager

AGENT=${1:-ai-cto}
SESSION_NUM=${2:-1}
DATE=$(date +%Y-%m-%d)
BRANCH="session/$AGENT/$DATE-$SESSION_NUM"

# Validate agent exists
if [ ! -d ".ai/agents/$AGENT" ]; then
    echo "❌ Agent $AGENT not configured in this project"
    echo "Available agents:"
    ls .ai/agents/
    exit 1
fi

echo "🚀 Starting session $SESSION_NUM for $AGENT"
echo "📍 Branch: $BRANCH"

# Update agent state
jq ".last_session = \"$DATE-$SESSION_NUM\" | .total_sessions += 1" \
    .ai/agents/$AGENT/state.json > tmp.json && mv tmp.json .ai/agents/$AGENT/state.json

# Create session branch
git checkout -b "$BRANCH" 2>/dev/null || git checkout "$BRANCH"

# Start session timer
START_TIME=$(date +%s)
echo "⏱️  Session started at $(date '+%H:%M')"
echo "📋 Remember: 60-90 minute focus"
echo ""
echo "Agent: $AGENT is ready to work!"

# Background timer
(sleep 5400 && echo -e "\n⏰ 90 minutes elapsed - time to wrap up and extract patterns!") &
EOF
chmod +x scripts/session-manager.sh

# Create metrics dashboard inline
cat > scripts/metrics-dashboard.sh << 'EOFMETRICS'
#!/bin/bash
# AADF Metrics Dashboard

echo "📊 AADF Metrics Dashboard"
echo "========================"
echo ""

# Git metrics
echo "📈 Git Activity:"
echo "- Commits today: $(git log --since=midnight --oneline 2>/dev/null | wc -l)"
echo "- Total commits: $(git rev-list --all --count 2>/dev/null || echo 0)"
echo "- Current branch: $(git branch --show-current 2>/dev/null || echo 'main')"
echo ""

# Agent metrics
echo "🤖 Agent Activity:"
for agent in .ai/agents/*; do
    if [ -d "$agent" ]; then
        agent_name=$(basename "$agent")
        if [ -f "$agent/state.json" ]; then
            sessions=$(jq -r '.total_sessions // 0' "$agent/state.json")
            echo "- $agent_name: $sessions sessions"
        fi
    fi
done
echo ""

# File metrics
echo "📁 Project Stats:"
echo "- Files: $(find . -type f -name "*.ts" -o -name "*.js" -o -name "*.py" 2>/dev/null | wc -l)"
echo "- Lines of code: $(find . -type f \( -name "*.ts" -o -name "*.js" -o -name "*.py" \) -exec wc -l {} + 2>/dev/null | tail -1 | awk '{print $1}')"
echo ""

# Pattern discoveries
echo "💡 Pattern Discoveries:"
pattern_count=$(find .ai/patterns -name "*.json" 2>/dev/null | wc -l)
echo "- Total patterns: $pattern_count"
EOFMETRICS
chmod +x scripts/metrics-dashboard.sh

# Language-specific setup
case $PRIMARY_LANGUAGE in
    "typescript"|"javascript")
        # Create package.json for TS/JS projects
        npm init -y
        npm pkg set name="$PROJECT_NAME"
        npm pkg set scripts.dev="echo 'Configure dev script'"
        npm pkg set scripts.test="echo 'Configure test script'"
        
        if [ "$PRIMARY_LANGUAGE" == "typescript" ]; then
            # Add TypeScript
            npm install -D typescript @types/node
            npx tsc --init --strict
        fi
        ;;
    "python")
        # Create Python project structure
        cat > requirements.txt << EOF
# Add your dependencies here
pytest>=7.0.0
black>=22.0.0
mypy>=1.0.0
EOF
        cat > pyproject.toml << EOF
[tool.black]
line-length = 88

[tool.mypy]
strict = true
EOF
        ;;
    "go")
        # Initialize Go module
        go mod init "$PROJECT_NAME"
        ;;
    "rust")
        # Create Rust project
        cargo init --name "$PROJECT_NAME"
        ;;
esac

# Initialize git repository
echo -e "${GREEN}📦 Initializing git repository...${NC}"
git init
git add .
git commit -m "feat: initialize $PROJECT_NAME with AADF framework

- Project type: $PROJECT_TYPE
- Language: $PRIMARY_LANGUAGE  
- AI agents configured: ${SELECTED_AGENTS[*]}
- A2A v5 messaging ready
- Session management ready
- Metrics tracking ready

Starting at 10x with path to 48x acceleration"

if [ -n "$GITHUB_ORG" ]; then
    git remote add origin "https://github.com/$GITHUB_ORG/$PROJECT_NAME.git"
fi

# Final setup
echo -e "\n${GREEN}✅ AADF Project Created Successfully!${NC}"
echo -e "${BLUE}═══════════════════════════════════════════════════════════════${NC}"
echo -e "📍 Location: ${YELLOW}$PROJECT_DIR${NC}"
echo -e "🤖 Agents: ${YELLOW}${SELECTED_AGENTS[*]}${NC}"
echo -e "🎯 Starting at: ${GREEN}10x productivity${NC}"
if [[ "$ENABLE_AUTOMATION" == "Y" ]] || [[ "$ENABLE_AUTOMATION" == "y" ]]; then
    echo -e "🤖 Automation: ${GREEN}ENABLED${NC} - Autonomous development ready!"
fi
echo -e "${BLUE}═══════════════════════════════════════════════════════════════${NC}"

echo -e "\n${CYAN}Next Steps:${NC}"
echo "1. cd $PROJECT_DIR"
if [[ "$ENABLE_AUTOMATION" == "Y" ]] || [[ "$ENABLE_AUTOMATION" == "y" ]]; then
    echo "2. Start automation:"
    echo "   ./scripts/automation/start-automation.sh"
    echo "3. Monitor activity:"
    echo "   python3 scripts/automation/monitoring/dashboard.py"
    echo "4. Or work manually:"
    echo "   ./scripts/session-manager.sh ${SELECTED_AGENTS[0]} 1"
else
    echo "2. Start your first session:"
    echo "   ./scripts/session-manager.sh ${SELECTED_AGENTS[0]} 1"
    echo "3. Check agent configurations:"
    echo "   cat .ai/agents/*/config.json"
    echo "4. Begin development with your AI team!"
fi
echo ""
if [[ "$ENABLE_AUTOMATION" == "Y" ]] || [[ "$ENABLE_AUTOMATION" == "y" ]]; then
    echo -e "${GREEN}🚀 You're starting at 10x with AUTONOMOUS agents!${NC}"
    echo -e "${YELLOW}💡 Push a commit and watch your AI team spring into action!${NC}"
else
    echo -e "${GREEN}🚀 You're starting at 10x. Your AI team is ready!${NC}"
fi
EOF

