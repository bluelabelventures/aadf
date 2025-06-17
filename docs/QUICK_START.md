# AADF Quick Start Guide: Zero to Autonomous in 5 Minutes
## Step-by-Step Project Launch with AI Teams

### Prerequisites

- Git installed
- Python 3.8+ (for automation features)
- Terminal/command line access
- AI API keys (Claude, GPT-4, or local LLMs)

### Step 1: Get the Launcher

```bash
# Clone the AADF repository
git clone https://github.com/bluelabelventures/aadf.git
cd aadf

# Make launcher executable
chmod +x launcher.sh
```

### Step 2: Run the Universal Launcher

```bash
./launcher.sh
```

You'll see:
```
╔═══════════════════════════════════════════════════════════════╗
║          AADF Universal Project Launcher v1.0.0               ║
║      Start ANY project at 10x with AI agent teams            ║
╚═══════════════════════════════════════════════════════════════╝
```

### Step 3: Configure Your Project

The launcher will guide you through 6 steps:

#### Step 1: Project Basics
```
Project name: my-awesome-app
Project directory (default: ~/my-awesome-app): [Enter]
GitHub organization (optional): mycompany
```

#### Step 2: Project Type
```
1) Web Application (Next.js)
2) API Service (Node/Express)
3) CLI Tool
4) Mobile App (React Native)
5) Machine Learning Pipeline
6) Documentation Site
7) Custom

Select project type [1-7]: 1
```

#### Step 3: Primary Language
```
1) TypeScript (recommended)
2) JavaScript
3) Python
4) Go
5) Rust

Select primary language [1-5]: 1
```

#### Step 4: AI Agent Team
```
1) Solo (Just AI-CTO)
2) Small Team (CTO + 2 specialists)
3) Full Team (CTO + 4-5 specialists)
4) Custom Selection

Select team size [1-4]: 3
```

This gives you:
- **AI-CTO**: Technical leadership
- **AI-Frontend**: UI/UX specialist
- **AI-Backend**: API/Database specialist
- **AI-QA**: Testing specialist
- **AI-DevOps**: Infrastructure specialist

#### Step 5: Enable Automation (NEW!)
```
Enable autonomous development with event-driven automation?
This includes:
  • Git event detection (commits, PRs, issues)
  • Automatic task assignment to agents
  • Real-time orchestration
  • Activity dashboard

Enable automation? [Y/n]: Y
```

**Always choose Y for autonomous development!**

#### Step 6: Confirm Configuration
```
Project Name: my-awesome-app
Directory: ~/my-awesome-app
Type: web-app
Language: typescript
Agents: ai-cto ai-frontend ai-backend ai-qa ai-devops
GitHub Org: mycompany
Automation: Enabled

Proceed with creation? [Y/n]: Y
```

### Step 4: Project Creation

The launcher will now:
1. Create directory structure
2. Install A2A v5 messaging
3. Configure AI agents
4. Set up automation framework
5. Initialize git repository
6. Create first commit

You'll see:
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

Navigate to your project and start automation:

```bash
cd ~/my-awesome-app

# Start the automation system
./scripts/automation/start-automation.sh
```

Output:
```
🚀 Starting AADF Automation System
==================================
Starting git event watcher...
Starting task orchestrator...
✅ Automation started!

Monitor with: python3 scripts/automation/monitoring/dashboard.py
Stop with: ./scripts/automation/stop-automation.sh
```

### Step 6: Trigger Your First Autonomous Action

Make a change to trigger the AI team:

```bash
# Create a simple TODO
echo "TODO: Add user authentication system" > TODO.md
git add TODO.md
git commit -m "docs: add authentication todo"
```

**What happens automatically:**
1. Git watcher detects the commit
2. Orchestrator creates task for AI-CTO
3. AI-CTO reviews and assigns subtasks:
   - AI-Backend: Design auth API
   - AI-Frontend: Create login UI
   - AI-QA: Write auth tests
4. Agents start working autonomously!

### Step 7: Monitor Your AI Team

Open a new terminal and run the dashboard:

```bash
cd ~/my-awesome-app
python3 scripts/automation/monitoring/dashboard.py
```

You'll see:
```
🤖 AADF AUTOMATION DASHBOARD
================================
Events Processed:          1
Tasks Created:             4
Tasks Completed:           0
Automation Rate:        100%
Current Acceleration:   10x

📥 RECENT EVENTS
16:45:32 | NEW_COMMIT | 🟡 HIGH

⚡ ACTIVE TASKS
⏳ [ai-cto] Review authentication requirements
📋 [ai-backend] Design authentication API
📋 [ai-frontend] Create login components
📋 [ai-qa] Plan authentication test suite
```

### Step 8: Check Agent Communications

See what your AI agents are discussing:

```bash
# Check CTO's inbox
./scripts/a2a-v5 inbox ai-cto

# See all recent messages
./scripts/a2a-v5 log
```

### Working with Your AI Team

#### Manual Sessions (When Needed)
```bash
# Start a focused session with an agent
./scripts/session-manager.sh ai-frontend 1

# Agent is now ready for direct collaboration
# Make changes, agent tracks everything
```

#### Autonomous Mode (Default)
- Just push commits - AI team responds
- Create issues - Automatically assigned
- Make PRs - AI reviews and tests
- Tests fail - AI debugs

### Project Structure Created

```
my-awesome-app/
├── .ai/                    # AI team headquarters
│   ├── agents/            # Agent configurations
│   ├── automation/        # Event logs and tasks
│   └── communication/     # A2A messaging
├── scripts/               
│   ├── automation/        # Automation framework
│   ├── a2a-v5            # Agent messaging
│   └── session-manager.sh # Manual sessions
├── src/                   # Your code (TypeScript)
├── package.json          # Dependencies
├── tsconfig.json         # TypeScript config
└── CLAUDE.md             # AI context document
```

### Common Workflows

#### 1. Add a New Feature
```bash
# Create feature request
echo "FEATURE: Add shopping cart" > features/cart.md
git add . && git commit -m "feat: shopping cart requirement"

# AI team automatically:
# - Designs architecture (AI-CTO)
# - Implements frontend (AI-Frontend)  
# - Creates API (AI-Backend)
# - Writes tests (AI-QA)
```

#### 2. Fix a Bug
```bash
# Report bug
echo "BUG: Login fails on mobile" > bugs/mobile-login.md
git add . && git commit -m "bug: mobile login issue"

# AI-QA investigates and assigns fix to appropriate agent
```

#### 3. Refactor Code
```bash
# Request refactor
git commit --allow-empty -m "refactor: optimize database queries"

# AI-Backend handles optimization
# AI-QA ensures nothing breaks
```

### Tips for Maximum Acceleration

1. **Clear Commit Messages**: Use semantic prefixes (feat:, fix:, docs:)
2. **Detailed TODOs**: More detail = better AI execution
3. **Trust the Automation**: Let AI work without interruption
4. **Review in Batches**: Check progress every few hours
5. **Use the Dashboard**: Monitor don't micromanage

### Troubleshooting

#### Automation Not Starting?
```bash
# Check Python version
python3 --version  # Need 3.8+

# Check logs
cat .ai/automation/logs/orchestrator.log
```

#### Agents Not Responding?
```bash
# Check A2A messaging
./scripts/a2a-v5 test

# Restart automation
./scripts/automation/stop-automation.sh
./scripts/automation/start-automation.sh
```

#### Need to Stop Everything?
```bash
# Stop automation
./scripts/automation/stop-automation.sh

# Work manually if needed
./scripts/session-manager.sh ai-cto 1
```

### What's Next?

1. **Push More Commits**: Watch your AI team respond
2. **Create Issues**: See automatic assignment
3. **Monitor Progress**: Use dashboard regularly
4. **Extract Patterns**: AI learns and accelerates
5. **Share Success**: Tell others about 10x→500x journey

### Congratulations! 🎉

You now have an autonomous AI development team working on your project. You've gone from zero to:
- ✅ Full project structure
- ✅ 5 specialized AI agents
- ✅ Autonomous task execution
- ✅ 10x baseline productivity
- ✅ Path to 500x acceleration

**Remember**: You're now the visionary CEO. Let your AI team handle the implementation while you focus on what to build, not how to build it.

---

*Welcome to the future of software development. It's autonomous.*