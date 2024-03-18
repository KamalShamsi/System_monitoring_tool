# System Monitoring Tool

## Description
This tool monitors and logs system performance metrics, including CPU usage, memory usage, disk usage, process count, and the top processes by CPU and memory usage.

## Setup
1. Ensure Python 3 and pip are installed.
2. Install the `psutil` package: `pip install psutil`
3. Run the script: `python monitor.py`

## Output
The output is logged to `system_log.txt`, appending new entries with a timestamp.

## Functionality
- `get_system_info()`: Retrieves overall system usage statistics.
- `write_to_file(info)`: Appends the information to the log file with a timestamp.
- `get_top_processes_by_cpu(n)`: Retrieves the top `n` processes by CPU usage.
- `get_top_processes_by_memory(n)`: Retrieves the top `n` processes by memory usage.

## Error Handling
The script includes error handling to continue operation even if some metrics cannot be retrieved.

## Automation
To automate the monitoring, set up a cron job to run this script at your desired intervals.
