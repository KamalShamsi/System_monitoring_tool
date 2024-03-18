import psutil
import datetime

def get_system_info():
    try:
        cpu_usage = psutil.cpu_percent(interval=1)
        memory_usage = psutil.virtual_memory().percent
        disk_usage = psutil.disk_usage('/').percent
        process_count = len(psutil.pids())
        return cpu_usage, memory_usage, disk_usage, process_count
    except Exception as e:
        return f"Error getting system info: {e}"

def write_to_file(info):
    try:
        with open("system_log.txt", "a") as log_file:
            timestamp = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
            if not isinstance(info, str):
                log_file.write(f"{timestamp} - CPU: {info[0]}%, Memory: {info[1]}%, Disk: {info[2]}%, Processes: {info[3]}\n")
            else:
                log_file.write(f"{timestamp} - {info}\n")
    except Exception as e:
        print(f"Error writing to file: {e}")

try:
    info = get_system_info()
    write_to_file(info)
except Exception as e:
    print(f"An error occurred: {e}")
