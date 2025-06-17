# Complete Guide: Launch a New AADF Project from Zero
## Everything You Need to Start Building with Autonomous AI Teams

### Table of Contents
1. [What is AADF?](#what-is-aadf)
2. [Prerequisites](#prerequisites)
3. [Step-by-Step Launch](#step-by-step-launch)
4. [Understanding Your AI Team](#understanding-your-ai-team)
5. [Working with Automation](#working-with-automation)
6. [Common Workflows](#common-workflows)
7. [Troubleshooting](#troubleshooting)
8. [Advanced Topics](#advanced-topics)

---

## What is AADF?

AADF (AI-Accelerated Development Framework) is a complete system for building software with autonomous AI teams. Instead of one developer or one AI assistant, you get a full team of specialized AI agents that work together automatically.

**Key Benefits:**
- Start at 10x productivity immediately
- Scale to 48x with patterns (proven)
- Path to 500x with full automation
- Zero configuration required
- Works with any project type

---

## Prerequisites

Before starting, ensure you have:

1. **Git** installed
   ```bash
   git --version  # Should show 2.0 or higher
   ```

2. **Python 3.8+** (for automation features)
   ```bash
   python3 --version  # Should show 3.8 or higher
   ```

3. **Terminal/Command Line** access

4. **AI API Access** (one of):
   - Claude API key (recommended)
   - OpenAI API key
   - Local LLM setup (Ollama)

---

## Step-by-Step Launch

### Step 1: Get AADF

```bash
# Clone the AADF framework
git clone https://github.com/bluelabelventures/aadf.git
cd aadf

# Make launcher executable
chmod +x launcher.sh
```

### Step 2: Run the Universal Launcher

```bash
./launcher.sh
```

You'll see a welcome screen:
```
╔═══════════════════════════════════════════════════════════════╗
║          AADF Universal Project Launcher v1.0.0               ║
║      Start ANY project at 10x with AI agent teams            ║
╚═══════════════════════════════════════════════════════════════╝
```

### Step 3: Configure Your Project

The launcher will walk you through 6 interactive steps:

#### 3.1 Project Basics
```
Step 1: Project Basics
Project name: my-awesome-app
Project directory (default: ~/my-awesome-app): [Press Enter]
GitHub organization (optional): [Press Enter to skip]
```

#### 3.2 Choose Project Type
```
Step 2: Project Type
1) Web Application (Next.js)
2) API Service (Node/Express)
3) CLI Tool
4) Mobile App (React Native)
5) Machine Learning Pipeline
6) Documentation Site
7) Custom

Select project type [1-7]: 1
```

#### 3.3 Select Language
```
Step 3: Primary Language
1) TypeScript (recommended)
2) JavaScript
3) Python
4) Go
5) Rust

Select primary language [1-5]: 1
```

#### 3.4 Choose AI Team Size
```
Step 4: AI Agent Team
1) Solo (Just AI-CTO)
2) Small Team (CTO + 2 specialists)
3) Full Team (CTO + 4-5 specialists)
4) Custom Selection

Select team size [1-4]: 3
```

**Full Team includes:**
- **AI-CTO**: Technical leadership and coordination
- **AI-Frontend**: UI/UX implementation
- **AI-Backend**: API and database work
- **AI-QA**: Testing and quality assurance
- **AI-DevOps**: Infrastructure and deployment

#### 3.5 Enable Automation (IMPORTANT!)
```
Step 5: Event-Driven Automation
Enable autonomous development with event-driven automation?
This includes:
  • Git event detection (commits, PRs, issues)
  • Automatic task assignment to agents
  • Real-time orchestration
  • Activity dashboard

Enable automation? [Y/n]: Y
```

**Always choose Y for autonomous development!**

#### 3.6 Confirm Settings
```
Step 6: Configuration Summary
Project Name: my-awesome-app
Directory: ~/my-awesome-app
Type: web-app
Language: typescript
Agents: ai-cto ai-frontend ai-backend ai-qa ai-devops
GitHub Org: none
Automation: Enabled

Proceed with creation? [Y/n]: Y
```

### Step 4: Automatic Project Creation

The launcher now creates everything:
```
🚀 Creating AADF Project...
📁 Creating AADF directories...
📬 Installing A2A v5...
🤖 Installing automation framework...
🤖 Configuring AI agents...
📦 Initializing git repository...

✅ AADF Project Created Successfully!
═══════════════════════════════════════════════════════════════
📍 Location: ~/my-awesome-app
🤖 Agents: ai-cto ai-frontend ai-backend ai-qa ai-devops
🎯 Starting at: 10x productivity
🤖 Automation: ENABLED - Autonomous development ready!
═══════════════════════════════════════════════════════════════
```

### Step 5: Start Autonomous Development

Navigate to your project:
```bash
cd ~/my-awesome-app
```

Start the automation system:
```bash
./scripts/automation/start-automation.sh
```

You'll see:
```
🚀 Starting AADF Automation System
==================================
Starting git event watcher...
Starting task orchestrator...
✅ Automation started!

Monitor with: python3 scripts/automation/monitoring/dashboard.py
Stop with: ./scripts/automation/stop-automation.sh
```

### Step 6: Trigger Your AI Team

Make any change to activate your AI team:

```bash
# Create a TODO file
echo "TODO: Build user authentication system" > TODO.md

# Commit it
git add TODO.md
git commit -m "docs: add authentication requirements"
```

**What happens automatically:**
1. Git watcher detects your commit
2. Orchestrator analyzes the change
3. AI-CTO receives the task
4. CTO breaks it down and assigns to team:
   - Backend: Design auth API
   - Frontend: Create login UI
   - QA: Plan test strategy
5. All agents start working in parallel!

### Step 7: Monitor Progress

In a new terminal:
```bash
cd ~/my-awesome-app
python3 scripts/automation/monitoring/dashboard.py
```

You'll see real-time activity:
```
🤖 AADF AUTOMATION DASHBOARD
================================
Events Processed:         1
Tasks Created:           4
Tasks Completed:         0
Automation Rate:     100%
Current Acceleration: 10x

📥 RECENT EVENTS
10:45:32 | NEW_COMMIT | 🟡 HIGH

⚡ ACTIVE TASKS
⏳ [ai-cto] Review authentication requirements
📋 [ai-backend] Design auth API endpoints
📋 [ai-frontend] Create login component
📋 [ai-qa] Write auth test plan
```

---

## Understanding Your AI Team

### Agent Roles

1. **AI-CTO** (Chief Technology Officer)
   - Reviews all commits
   - Makes architecture decisions
   - Assigns tasks to other agents
   - Handles complex problems

2. **AI-Frontend** (UI/UX Specialist)
   - Implements user interfaces
   - Handles styling and responsiveness
   - Creates components
   - Manages user experience

3. **AI-Backend** (API/Database Expert)
   - Designs APIs
   - Implements business logic
   - Manages databases
   - Handles integrations

4. **AI-QA** (Quality Assurance)
   - Writes tests
   - Finds bugs
   - Ensures code quality
   - Validates features

5. **AI-DevOps** (Infrastructure)
   - Sets up CI/CD
   - Manages deployments
   - Monitors performance
   - Handles scaling

### How They Communicate

Agents use A2A (Agent-to-Agent) messaging:

```bash
# View all messages
./scripts/a2a-v5 log

# Check specific agent's inbox
./scripts/a2a-v5 inbox ai-cto

# See message details
./scripts/a2a-v5 read <message-id>
```

---

## Working with Automation

### Automation Triggers

Your AI team responds to:

1. **Git Commits**
   ```bash
   git commit -m "feat: add shopping cart"
   # → AI team implements the feature
   ```

2. **Pull Requests**
   ```bash
   git checkout -b feature/payments
   # Make changes
   git push origin feature/payments
   # → AI-QA reviews and tests
   ```

3. **Issues** (if using GitHub)
   ```bash
   # Create issue on GitHub
   # → AI-CTO triages and assigns
   ```

4. **Test Failures**
   ```bash
   npm test  # If tests fail
   # → AI-QA investigates and fixes
   ```

### Manual Control

You can always work directly with agents:

```bash
# Start a manual session
./scripts/session-manager.sh ai-frontend 1

# Now work directly with that agent
# Make changes, agent tracks everything
```

---

## Common Workflows

### Adding a Feature

1. **Describe what you want**
   ```bash
   echo "FEATURE: User profile page with edit capability" > features/profile.md
   git add . && git commit -m "feat: user profile requirements"
   ```

2. **AI team automatically:**
   - CTO designs architecture
   - Frontend creates UI
   - Backend implements API
   - QA writes tests

3. **Review the work**
   ```bash
   # Check what was built
   git log --oneline
   
   # Review code changes
   git diff HEAD~5
   ```

### Fixing a Bug

1. **Report the bug**
   ```bash
   echo "BUG: Login button not working on mobile" > bugs/mobile-login.md
   git add . && git commit -m "bug: mobile login issue"
   ```

2. **AI team responds:**
   - QA investigates
   - Assigns to appropriate agent
   - Fix is implemented
   - Tests are added

### Refactoring Code

```bash
# Request refactoring
git commit --allow-empty -m "refactor: optimize database queries"

# AI-Backend handles the refactoring
# AI-QA ensures nothing breaks
```

---

## Troubleshooting

### Automation Not Working?

1. **Check Python version**
   ```bash
   python3 --version  # Must be 3.8+
   ```

2. **View logs**
   ```bash
   cat .ai/automation/logs/orchestrator.log
   cat .ai/automation/logs/git-watcher.log
   ```

3. **Restart automation**
   ```bash
   ./scripts/automation/stop-automation.sh
   ./scripts/automation/start-automation.sh
   ```

### Agents Not Responding?

1. **Check A2A system**
   ```bash
   ./scripts/a2a-v5 test
   ```

2. **Verify agent configuration**
   ```bash
   cat .ai/agents/ai-cto/config.json
   ```

3. **Check for messages**
   ```bash
   ./scripts/a2a-v5 inbox ai-cto
   ```

### Need to Stop Everything?

```bash
# Stop automation
./scripts/automation/stop-automation.sh

# Work manually
./scripts/session-manager.sh ai-cto 1
```

---

## Advanced Topics

### Customizing Agent Behavior

Edit agent configurations in `.ai/agents/*/config.json`:
```json
{
  "role": "ai-frontend",
  "preferences": {
    "framework": "react",
    "styling": "tailwind",
    "testing": "jest"
  }
}
```

### Adding New Event Handlers

Edit `scripts/automation/orchestrator-config.json`:
```json
{
  "event_handlers": {
    "custom_event": {
      "assignee": "ai-cto",
      "priority": "HIGH"
    }
  }
}
```

### Creating Custom Agents

1. Add agent configuration to `.ai/agents/`
2. Update orchestrator config
3. Restart automation

### Extracting Patterns

After successful implementations:
```bash
# Document the pattern
echo "PATTERN: Component testing approach" > .ai/patterns/testing-pattern.md

# AI team will reuse this pattern in future
```

---

## Summary

You now have:
- ✅ A fully configured project
- ✅ 5 specialized AI agents
- ✅ Autonomous task execution
- ✅ 10x baseline productivity
- ✅ Clear path to 500x

**Remember**: You're now the CEO/Visionary. Focus on WHAT to build, let your AI team handle HOW to build it.

**Next steps:**
1. Make more commits and watch AI respond
2. Create issues for AI to handle
3. Monitor the dashboard regularly
4. Extract patterns as you go
5. Share your acceleration story!

---

*Welcome to autonomous development. The future is here.*