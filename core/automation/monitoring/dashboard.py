#!/usr/bin/env python3
"""
AADF Automation Dashboard
Real-time monitoring of autonomous AI orchestration
"""

import os
import sys
import time
import json
from datetime import datetime, timedelta
from pathlib import Path
from typing import Dict, List

# Simple terminal-based dashboard (no external dependencies)


class AutomationDashboard:
    """Terminal-based dashboard for monitoring AADF automation"""
    
    def __init__(self):
        self.metrics = {
            "start_time": datetime.now(),
            "events_processed": 0,
            "tasks_created": 0,
            "tasks_completed": 0,
            "automation_rate": 0.0,
            "average_response_time": 0.0,
            "human_interventions": 0,
            "cost_estimate": 0.0
        }
        
        self.recent_events = []  # Last 10 events
        self.active_tasks = []
        self.acceleration_history = []
        
    def clear_screen(self):
        """Clear terminal screen"""
        os.system('clear' if os.name == 'posix' else 'cls')
    
    def format_duration(self, duration: timedelta) -> str:
        """Format duration as human-readable string"""
        total_seconds = int(duration.total_seconds())
        hours = total_seconds // 3600
        minutes = (total_seconds % 3600) // 60
        seconds = total_seconds % 60
        
        if hours > 0:
            return f"{hours}h {minutes}m {seconds}s"
        elif minutes > 0:
            return f"{minutes}m {seconds}s"
        else:
            return f"{seconds}s"
    
    def render_header(self):
        """Render dashboard header"""
        print("=" * 80)
        print("🤖 AADF AUTOMATION DASHBOARD".center(80))
        print("=" * 80)
        
        uptime = datetime.now() - self.metrics["start_time"]
        print(f"Uptime: {self.format_duration(uptime)}")
        print(f"Time: {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}")
        print("=" * 80)
    
    def render_metrics(self):
        """Render key metrics section"""
        print("\n📊 KEY METRICS")
        print("-" * 40)
        
        # Calculate current acceleration
        baseline_time = 4 * 60  # 4 hours in minutes
        current_time = self.metrics["average_response_time"] / 60 if self.metrics["average_response_time"] > 0 else baseline_time
        acceleration = baseline_time / current_time if current_time > 0 else 1.0
        
        print(f"Events Processed:     {self.metrics['events_processed']:>10}")
        print(f"Tasks Created:        {self.metrics['tasks_created']:>10}")
        print(f"Tasks Completed:      {self.metrics['tasks_completed']:>10}")
        print(f"Automation Rate:      {self.metrics['automation_rate']:>9.1f}%")
        print(f"Avg Response Time:    {self.metrics['average_response_time']:>9.1f}s")
        print(f"Current Acceleration: {acceleration:>9.1f}x")
        print(f"Human Interventions:  {self.metrics['human_interventions']:>10}")
        print(f"Est. Cost Today:      ${self.metrics['cost_estimate']:>9.2f}")
    
    def render_recent_events(self):
        """Render recent events section"""
        print("\n📥 RECENT EVENTS (Last 5)")
        print("-" * 60)
        
        if not self.recent_events:
            print("No events yet...")
        else:
            for event in self.recent_events[-5:]:
                timestamp = event.get('timestamp', 'Unknown')
                event_type = event.get('type', 'Unknown')
                priority = event.get('priority', 'Unknown')
                
                # Color code by priority
                if priority == 'CRITICAL':
                    priority_str = "🔴 CRITICAL"
                elif priority == 'HIGH':
                    priority_str = "🟡 HIGH"
                else:
                    priority_str = "🟢 " + priority
                
                print(f"{timestamp} | {event_type:<20} | {priority_str}")
    
    def render_active_tasks(self):
        """Render active tasks section"""
        print("\n⚡ ACTIVE TASKS")
        print("-" * 60)
        
        if not self.active_tasks:
            print("No active tasks...")
        else:
            for task in self.active_tasks[:5]:
                agent = task.get('agent', 'Unknown')
                description = task.get('description', 'Unknown')[:40]
                status = task.get('status', 'Pending')
                
                status_emoji = "⏳" if status == "In Progress" else "📋"
                print(f"{status_emoji} [{agent:<15}] {description}")
    
    def render_acceleration_graph(self):
        """Render simple ASCII acceleration graph"""
        print("\n📈 ACCELERATION TREND (Last 10 measurements)")
        print("-" * 60)
        
        if not self.acceleration_history:
            print("Gathering data...")
        else:
            # Simple ASCII bar chart
            max_accel = max(self.acceleration_history[-10:]) if self.acceleration_history else 50
            
            for i, accel in enumerate(self.acceleration_history[-10:]):
                bar_length = int((accel / max_accel) * 40)
                bar = "█" * bar_length
                print(f"{i+1:2d}: {bar} {accel:.1f}x")
    
    def render_status_indicators(self):
        """Render system status indicators"""
        print("\n🚦 SYSTEM STATUS")
        print("-" * 40)
        
        # Git Watcher Status
        git_watcher_status = "🟢 Active" if self.check_git_watcher() else "🔴 Inactive"
        print(f"Git Watcher:    {git_watcher_status}")
        
        # Orchestrator Status
        orchestrator_status = "🟢 Active" if self.check_orchestrator() else "🔴 Inactive"
        print(f"Orchestrator:   {orchestrator_status}")
        
        # A2A Status
        a2a_status = "🟢 Connected" if self.check_a2a() else "🟡 Degraded"
        print(f"A2A Messaging:  {a2a_status}")
        
        # Cost Status
        daily_limit = 100.0
        cost_status = "🟢 Normal" if self.metrics['cost_estimate'] < daily_limit * 0.8 else "🟡 Warning"
        print(f"Cost Control:   {cost_status}")
    
    def check_git_watcher(self) -> bool:
        """Check if git watcher is running"""
        # Check for recent event files
        event_dir = Path("/tmp")
        recent_events = list(event_dir.glob("aadf-event-*.json"))
        
        if recent_events:
            # Check if any event is recent (within last minute)
            for event_file in recent_events:
                if time.time() - event_file.stat().st_mtime < 60:
                    return True
        
        return False
    
    def check_orchestrator(self) -> bool:
        """Check if orchestrator is running"""
        # In production, would check process or heartbeat
        return True  # Placeholder
    
    def check_a2a(self) -> bool:
        """Check A2A messaging status"""
        # In production, would check A2A health
        return True  # Placeholder
    
    def render_footer(self):
        """Render dashboard footer"""
        print("\n" + "=" * 80)
        print("Commands: [q]uit | [r]efresh | [p]ause automation | [m]etrics detail")
        print("=" * 80)
    
    def render(self):
        """Render complete dashboard"""
        self.clear_screen()
        self.render_header()
        self.render_metrics()
        self.render_recent_events()
        self.render_active_tasks()
        self.render_acceleration_graph()
        self.render_status_indicators()
        self.render_footer()
    
    def update_metrics(self, new_metrics: Dict):
        """Update metrics from external source"""
        self.metrics.update(new_metrics)
    
    def add_event(self, event: Dict):
        """Add new event to recent events"""
        event['timestamp'] = datetime.now().strftime('%H:%M:%S')
        self.recent_events.append(event)
        
        # Keep only last 20 events
        if len(self.recent_events) > 20:
            self.recent_events = self.recent_events[-20:]
    
    def update_tasks(self, tasks: List[Dict]):
        """Update active tasks list"""
        self.active_tasks = tasks
    
    def add_acceleration_measurement(self, acceleration: float):
        """Add acceleration measurement to history"""
        self.acceleration_history.append(acceleration)
        
        # Keep only last 100 measurements
        if len(self.acceleration_history) > 100:
            self.acceleration_history = self.acceleration_history[-100:]
    
    def simulate_data(self):
        """Simulate data updates for demo purposes"""
        import random
        
        # Simulate metrics
        self.metrics['events_processed'] += random.randint(0, 2)
        self.metrics['tasks_created'] += random.randint(0, 3)
        self.metrics['tasks_completed'] += random.randint(0, 2)
        
        if self.metrics['tasks_created'] > 0:
            self.metrics['automation_rate'] = (
                self.metrics['tasks_completed'] / self.metrics['tasks_created'] * 100
            )
        
        self.metrics['average_response_time'] = random.uniform(2.0, 5.0)
        self.metrics['cost_estimate'] += random.uniform(0.1, 0.5)
        
        # Simulate events
        if random.random() > 0.7:
            event_types = ['NEW_COMMIT', 'PATTERN_DISCOVERED', 'SESSION_START']
            priorities = ['LOW', 'MEDIUM', 'HIGH', 'CRITICAL']
            
            self.add_event({
                'type': random.choice(event_types),
                'priority': random.choice(priorities)
            })
        
        # Simulate tasks
        if random.random() > 0.8:
            agents = ['cto', 'framework-architect', 'strategic-advisor']
            descriptions = [
                'Extract patterns from recent commit',
                'Review code changes in feature branch',
                'Update documentation for new patterns',
                'Analyze acceleration metrics',
                'Plan next development session'
            ]
            
            new_task = {
                'agent': random.choice(agents),
                'description': random.choice(descriptions),
                'status': 'In Progress'
            }
            
            self.active_tasks.append(new_task)
            
            # Remove completed tasks
            if len(self.active_tasks) > 5:
                self.active_tasks.pop(0)
        
        # Simulate acceleration
        current_accel = 48.0 + random.uniform(-5, 10)
        self.add_acceleration_measurement(current_accel)
    
    def run(self):
        """Run the dashboard with live updates"""
        print("Starting AADF Automation Dashboard...")
        print("Press 'q' to quit, 'r' to refresh")
        
        try:
            while True:
                # Render dashboard
                self.render()
                
                # Simulate data updates (in production, would read from real sources)
                self.simulate_data()
                
                # Wait before refresh
                time.sleep(5)
                
        except KeyboardInterrupt:
            print("\n\nDashboard stopped.")


def main():
    """Main entry point"""
    dashboard = AutomationDashboard()
    dashboard.run()


if __name__ == "__main__":
    main()