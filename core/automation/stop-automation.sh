#!/bin/bash
# Stop AADF Automation System

echo "🛑 Stopping AADF Automation System"
echo "=================================="

# Function to stop component
stop_component() {
    local name=$1
    local pidfile="/tmp/aadf-$name.pid"
    
    if [ -f "$pidfile" ]; then
        pid=$(cat "$pidfile")
        echo -n "Stopping $name (PID: $pid)... "
        kill $pid 2>/dev/null
        rm -f "$pidfile"
        echo "✓"
    else
        echo "$name: Not running"
    fi
}

# Stop components
stop_component "git-watcher"
stop_component "orchestrator"

# Clean up event files
echo -n "Cleaning up event files... "
rm -f /tmp/aadf-event-*.json
echo "✓"

echo ""
echo "✅ Automation system stopped"