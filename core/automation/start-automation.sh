#!/bin/bash
# AADF Automation Quick Start Script

echo "🚀 Starting AADF Automation System"
echo "=================================="

# Check Python version
python_version=$(python3 --version 2>&1 | awk '{print $2}')
echo "✓ Python version: $python_version"

# Set up environment
export PYTHONPATH="${PYTHONPATH}:$(pwd)"

# Create necessary directories
mkdir -p /tmp/aadf-events
echo "✓ Event directory created"

# Function to start component in background
start_component() {
    local name=$1
    local script=$2
    
    echo -n "Starting $name... "
    python3 $script > /tmp/aadf-$name.log 2>&1 &
    echo $! > /tmp/aadf-$name.pid
    echo "✓ (PID: $(cat /tmp/aadf-$name.pid))"
}

# Start components
echo ""
echo "Starting automation components:"
echo "------------------------------"

# Start Git Watcher
start_component "git-watcher" "event_detection/git_watcher.py"

# Wait a moment
sleep 2

# Start Orchestrator
start_component "orchestrator" "orchestration/orchestrator.py"

# Wait for components to initialize
sleep 2

echo ""
echo "✅ All components started!"
echo ""
echo "To monitor the system:"
echo "  python3 monitoring/dashboard.py"
echo ""
echo "To stop all components:"
echo "  ./stop-automation.sh"
echo ""
echo "Component logs:"
echo "  tail -f /tmp/aadf-git-watcher.log"
echo "  tail -f /tmp/aadf-orchestrator.log"
echo ""