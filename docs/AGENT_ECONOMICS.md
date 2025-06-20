# AADF Agent Economics - Smart Task Routing

## The Concept: Hierarchical AI Teams

AADF supports the idea of using different AI models based on task complexity:

### Senior Agents (Claude Opus, GPT-4)
- **ai-cto**: Architecture decisions, complex problems
- **ai-backend**: Critical API design, database architecture
- **ai-frontend**: Complex UI/UX challenges

### Mid-Level Agents (Claude Sonnet, GPT-3.5)
- **ai-qa**: Testing, code review
- **ai-devops**: Infrastructure setup, deployment

### Junior Agents (Claude Haiku, Free/Local LLMs)
- **ai-junior**: Simple tasks, documentation, refactoring
- Multiple juniors can work in parallel
- Perfect for repetitive or well-defined tasks

## How It's Supposed to Work

### 1. Task Complexity Detection
The orchestrator estimates complexity based on:
- Number of files changed
- Type of changes (new feature vs. refactor)
- Keywords in commit messages
- File types affected

### 2. Automatic Routing
```python
if complexity < 30:
    route_to("ai-junior")  # Use cheaper model
elif complexity < 70:
    route_to("ai-qa")      # Use mid-tier model  
else:
    route_to("ai-cto")     # Use premium model
```

### 3. Cost Optimization
- Junior tasks: ~$0.001 per task (using Haiku/local)
- Mid tasks: ~$0.01 per task (using Sonnet)
- Senior tasks: ~$0.10 per task (using Opus)

## Setting Up Tiered Agents

### Using Claude Code

#### Senior Agent Session
```bash
# For complex architecture decisions
claude-code --model claude-3-opus .

"I'm the ai-cto agent. Let's design the authentication system architecture."
```

#### Junior Agent Session
```bash
# For simple refactoring
claude-code --model claude-3-haiku .

"I'm an ai-junior agent. Please help me:
1. Add JSDoc comments to all functions in utils/
2. Fix ESLint warnings
3. Update import statements to use aliases"
```

### Using Cursor with Different Models

#### Configure Multiple Profiles
```
Profile: Senior Backend Dev
Model: GPT-4
Context: .ai/agents/ai-backend/

Profile: Junior Developer
Model: GPT-3.5-turbo
Context: .ai/agents/ai-junior/
Cost limit: $0.10/hour
```

### Using Local Models for Juniors

#### With Ollama
```bash
# Install Ollama and a model
ollama pull codellama

# Use for junior tasks
"You're an ai-junior agent. Task: Add type definitions to all exported functions."
```

#### With Continue.dev + Local LLM
Configure Continue to use local models for junior work

## Example: Smart Task Distribution

### Scenario: New Feature Request
"Add user profile page with avatar upload"

### How AADF Would Route This:

1. **ai-cto** (Opus/GPT-4): 
   - Design the overall architecture
   - Decide on avatar storage strategy
   - Define API contracts

2. **ai-backend** (Opus/GPT-4):
   - Implement avatar upload API
   - Set up S3/storage integration

3. **ai-frontend** (Sonnet/GPT-3.5):
   - Create the profile page UI
   - Implement upload component

4. **ai-junior** (Haiku/Local):
   - Add loading states
   - Write unit tests
   - Update documentation
   - Add accessibility attributes

### Cost Breakdown:
- Traditional (all GPT-4): ~$2.00
- With AADF routing: ~$0.50
- Savings: 75%

## Current Reality vs. Vision

### What Works Now:
- You can manually assign tasks to different agent roles
- You can use different models for different agents
- The structure supports this workflow

### What's Missing:
- Automatic complexity detection
- Automatic model selection
- True parallel execution
- Cost tracking

### Workaround for Now:
1. **Manually assess complexity** before starting sessions
2. **Choose appropriate model** based on task
3. **Use cheaper models** for junior work
4. **Track costs** yourself

## Best Practices

### 1. Start with Senior Agents
Let ai-cto break down the work into junior-friendly tasks

### 2. Batch Junior Work
Collect simple tasks and run them together:
```
"Here are 10 refactoring tasks for ai-junior:
1. Add types to user.js
2. Extract magic numbers to constants
3. ..."
```

### 3. Use Local LLMs for Repetitive Tasks
Perfect for:
- Adding comments
- Formatting code
- Simple refactors
- Writing basic tests

### 4. Reserve Premium Models for Complex Work
Use Opus/GPT-4 only for:
- Architecture decisions
- Complex algorithm design
- Security-critical code
- Performance optimization

## Future Vision

The full AADF vision includes:
- Automatic task complexity scoring
- Dynamic model selection
- Parallel junior agent execution
- Real-time cost optimization
- Learning which tasks suit which models

For now, you can achieve similar results manually by thoughtfully choosing which model to use for each task.