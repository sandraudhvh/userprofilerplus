import os
import json
import psutil
import platform
from datetime import datetime

class UserProfilerPlus:
    def __init__(self, user_id):
        self.user_id = user_id
        self.user_data_file = f"user_profile_{self.user_id}.json"
        self.user_data = self.load_user_data()

    def load_user_data(self):
        """Load user data from a JSON file, or create a new profile if it doesn't exist."""
        if os.path.exists(self.user_data_file):
            with open(self.user_data_file, 'r') as file:
                return json.load(file)
        else:
            return {
                "preferences": {},
                "usage_patterns": []
            }

    def save_user_data(self):
        """Save the user data to a JSON file."""
        with open(self.user_data_file, 'w') as file:
            json.dump(self.user_data, file, indent=4)

    def update_preferences(self, key, value):
        """Update the user's preferences."""
        self.user_data['preferences'][key] = value
        self.save_user_data()

    def track_usage(self):
        """Track usage patterns such as CPU and memory usage."""
        usage_info = {
            "timestamp": datetime.now().isoformat(),
            "cpu_usage": psutil.cpu_percent(interval=1),
            "memory_usage": psutil.virtual_memory().percent,
            "platform": platform.system(),
            "platform_version": platform.version()
        }
        self.user_data['usage_patterns'].append(usage_info)
        self.save_user_data()

    def display_user_profile(self):
        """Display the user's profile including preferences and usage patterns."""
        print(f"User ID: {self.user_id}")
        print("Preferences:")
        for key, value in self.user_data['preferences'].items():
            print(f"  {key}: {value}")
        print("Usage Patterns:")
        for usage in self.user_data['usage_patterns']:
            print(f"  - Timestamp: {usage['timestamp']}")
            print(f"    CPU Usage: {usage['cpu_usage']}%")
            print(f"    Memory Usage: {usage['memory_usage']}%")
            print(f"    Platform: {usage['platform']} {usage['platform_version']}")

# Example Usage:
if __name__ == "__main__":
    user_profiler = UserProfilerPlus(user_id='user123')
    user_profiler.update_preferences('theme', 'dark')
    user_profiler.track_usage()
    user_profiler.display_user_profile()