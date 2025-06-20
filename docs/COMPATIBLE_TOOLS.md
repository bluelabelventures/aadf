# Compatible AI Tools for AADF

AADF requires AI tools that can **read your local project files**. Here are the recommended options:

## ✅ Fully Compatible Tools

### Claude Code
- **Best for**: Full codebase access, file editing, terminal commands
- **How**: The official Anthropic coding assistant
- **Setup**: Just point it to your project directory

### Cursor
- **Best for**: IDE integration with AI agents
- **How**: Set up different agent profiles in Cursor
- **Setup**: 
  ```
  1. Open your AADF project in Cursor
  2. Create custom instructions for each agent role
  3. Switch between agent profiles as needed
  ```

### Windsurf
- **Best for**: AI-powered code editor workflow
- **How**: Configure AI agents within Windsurf
- **Setup**: Similar to Cursor, create agent-specific contexts

### Continue.dev
- **Best for**: VS Code users
- **How**: Install Continue extension in VS Code
- **Setup**: Configure different agent contexts

## ⚠️ Partially Compatible

### GitHub Copilot Chat (with workspace access)
- Can read files if you grant workspace access
- Limited compared to dedicated tools

### Cody (Sourcegraph)
- Can access codebase when properly configured
- Good for code search and understanding

## ❌ NOT Compatible

### ChatGPT
- **Why not**: Cannot read local files
- **Workaround**: You'd have to copy-paste everything manually (defeats the purpose)

### Claude.ai (web interface)
- **Why not**: Cannot access local files directly
- **Workaround**: Would require constant file uploads

### Google Bard/Gemini
- **Why not**: No local file access
- **Workaround**: Manual copy-paste only

## Recommended Workflow by Tool

### Using Claude Code
```bash
# In your project directory
claude-code .

# Then tell Claude:
"I'm the ai-frontend agent for this AADF project.
Please read my role from .ai/agents/ai-frontend/config.json"
```

### Using Cursor
```
1. File → Open Folder → Select your AADF project
2. Create a new AI chat
3. Add context: @codebase @file:.ai/agents/ai-backend/config.json
4. Start working as that agent
```

### Using Windsurf
```
1. Open project in Windsurf
2. Create agent-specific workspace
3. Reference the agent config files
4. Work within that agent's context
```

## Pro Tips

1. **Best Experience**: Claude Code - designed for this workflow
2. **Best IDE Integration**: Cursor - seamless editor experience
3. **Best for Teams**: Set up shared Cursor/Windsurf profiles for consistency
4. **Budget Option**: Continue.dev with local LLMs

## Setting Up Agent Profiles in Cursor

### Example: AI-Frontend Profile
```
Name: AADF Frontend Agent
Context: Always include .ai/agents/ai-frontend/
Instructions: 
- You are the ai-frontend agent
- Focus on UI/UX implementation
- Follow the patterns in .ai/patterns/
- Commit with semantic prefixes
```

### Example: AI-Backend Profile  
```
Name: AADF Backend Agent
Context: Always include .ai/agents/ai-backend/
Instructions:
- You are the ai-backend agent
- Focus on API and database design
- Check frontend contracts before changes
- Document all endpoints
```

## Why File Access Matters

AADF's value comes from:
- Reading agent configurations
- Seeing previous work in git history
- Accessing shared communication files
- Understanding project structure

Without file access, you lose all these benefits and might as well just use any AI without AADF.