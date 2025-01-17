# UserProfilerPlus

UserProfilerPlus is a Python program designed to extend user profile management on Windows systems by including detailed tracking of user preferences and usage patterns. This tool allows for the monitoring and logging of system resource usage, as well as the management of user-specific settings.

## Features

- **Preference Management**: Easily update and manage user-specific preferences.
- **Usage Tracking**: Monitor CPU and memory usage over time.
- **Cross-Platform Compatibility**: Designed to run on Windows systems.
- **JSON-Based Storage**: User profiles and usage data are stored in JSON format for easy access and manipulation.

## Installation

1. Ensure Python 3.x is installed on your system.
2. Install the required packages using pip:
   ```bash
   pip install psutil
   ```
3. Download or clone the repository containing the `user_profiler_plus.py` file.

## Usage

1. Import and instantiate the `UserProfilerPlus` class with a unique user ID:
    ```python
    from user_profiler_plus import UserProfilerPlus

    user_profiler = UserProfilerPlus(user_id='your_user_id')
    ```

2. Update user preferences:
    ```python
    user_profiler.update_preferences('theme', 'dark')
    ```

3. Track and log current system usage:
    ```python
    user_profiler.track_usage()
    ```

4. Display the user profile, including preferences and usage patterns:
    ```python
    user_profiler.display_user_profile()
    ```

## License

This project is licensed under the MIT License. See the LICENSE file for more information.

## Contributing

Contributions are welcome! Please feel free to submit a pull request or open an issue to improve this project.