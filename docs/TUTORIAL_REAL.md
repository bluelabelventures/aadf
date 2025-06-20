# AADF Real Tutorial - Building a Bookstore App

This tutorial shows you EXACTLY how AADF works in practice. No magic, no autonomous agents - just structured AI-assisted development.

## What We'll Build

A simple bookstore application with:
- Book listing page
- Add/edit books
- Search functionality

## Step 1: Create the Project (2 minutes)

```bash
# From the AADF directory
./launcher.sh

# Answer the prompts:
Project name: bookstore
Project directory: ./bookstore  # or wherever you want
Type: 1 (Web Application)
Language: typescript
Agents: ai-cto ai-frontend ai-backend
GitHub: (leave blank for now)
Enable automation: Y
```

This creates folders and config files. That's all.

## Step 2: First AI Session - Architecture (30 minutes)

### Open Claude or ChatGPT and start with:

```
I'm working on a bookstore web application using the AADF framework.
I'm acting as the ai-cto agent for this project.

My role (from .ai/agents/ai-cto/config.json) is:
- System architecture and technical decisions
- Code review and quality standards  
- Performance optimization strategies
- Security best practices
- Integration patterns

Let's design the architecture for a bookstore app that needs:
- Book inventory management
- Search functionality  
- Admin panel for adding/editing books
- Simple and clean UI

Please help me create:
1. A system architecture document
2. Technology stack recommendations
3. Project structure
```

### Work with the AI to create:
- `docs/architecture.md`
- `docs/tech-stack.md`
- Basic folder structure

### Commit your work:
```bash
git add .
git commit -m "feat: initial architecture design and tech stack"
```

## Step 3: Frontend Session (45 minutes)

### Open a NEW AI conversation and start with:

```
I'm working on a bookstore web application using the AADF framework.
I'm acting as the ai-frontend agent.

My role is to handle UI/UX implementation, responsive design, and component architecture.

Previous work by ai-cto:
- Architecture defined in docs/architecture.md
- Tech stack: Next.js, TypeScript, Tailwind CSS

Please help me:
1. Set up the Next.js project
2. Create the book listing page
3. Implement a clean, modern UI
```

### Work with the AI to:
- Initialize Next.js project
- Create components
- Style with Tailwind

### Commit progress:
```bash
git add .
git commit -m "feat: implement book listing UI with Next.js"
```

## Step 4: Backend Session (45 minutes)

### Open ANOTHER new AI conversation:

```
I'm the ai-backend agent for the bookstore project.

My role: API development, database design, server architecture.

Current state:
- Frontend created with Next.js (see previous commits)
- Need API for book CRUD operations

Please help me:
1. Create a REST API with Node.js/Express
2. Set up SQLite for simple data storage
3. Implement book CRUD endpoints
```

### Work with the AI to build the API

### Commit:
```bash
git add .
git commit -m "feat: implement book API with Express and SQLite"
```

## Step 5: Integration Session (30 minutes)

### Back to ai-frontend role in new conversation:

```
I'm ai-frontend again. The backend team has created an API.

Let me check what they built:
- API endpoints in api/routes/books.js
- Running on port 3001

Please help me:
1. Connect the frontend to the API
2. Implement data fetching
3. Handle loading and error states
```

## What's Really Happening?

1. **You** are driving everything
2. **AI assistants** help with implementation
3. **AADF** provides structure and context
4. **Git** preserves progress between sessions

## Measuring Your Success

After a few sessions, run:
```bash
./scripts/metrics-dashboard.sh
```

You'll see:
- Number of commits
- Lines of code written  
- Sessions completed
- Time saved vs. traditional development

## Common Confusions Cleared Up

### "Where are the autonomous agents?"
There aren't any. YOU run each AI session manually.

### "What does automation do?"
It watches for commits and creates task suggestions. It doesn't run AI.

### "How is this 48x faster?"
It's not, usually. Expect 5-10x improvement from:
- Better organization
- Preserved context
- Clear role definitions
- Structured workflow

### "Do I need special AI tools?"
No. Any AI assistant works (Claude, ChatGPT, Gemini, etc.)

## Tips for Success

1. **Keep sessions focused** - 60-90 minutes max
2. **Commit frequently** - Preserve context
3. **Use semantic commits** - feat:, fix:, docs:
4. **Switch roles** - Different perspectives help
5. **Review with ai-qa** - Catch issues early

## Real Productivity Gains

### Without AADF:
- 30 min: Explain context to AI
- 60 min: Development
- 30 min: Lost context, re-explain
- Total: 2 hours for one feature

### With AADF:
- 5 min: AI reads its role
- 55 min: Focused development  
- Next session continues smoothly
- Total: 1 hour for one feature

That's 2x speedup - realistic and valuable!

## Troubleshooting

### "AI doesn't understand its role"
Be explicit: "Read your configuration from .ai/agents/[agent-name]/config.json"

### "Lost context between sessions"  
Always commit your work. New sessions should run `git log` to see history.

### "Not seeing productivity gains"
It takes practice. First few sessions might be slower as you learn the workflow.

## Next Steps

1. Complete your bookstore app using this workflow
2. Try different AI assistants for different roles
3. Measure your actual productivity gains
4. Share your experience to help improve AADF

Remember: AADF is a workflow tool, not magic. Use it to structure your AI-assisted development, and you'll see real (not magical) productivity improvements!