import psutil
import datetime

def get_system_info():
    cpu_usage = psutil.cpu_percent(interval=1)
    memory_usage = psutil.virtual_memory().percent
    disk_usage = psutil.disk_usage('/').percent
    process_count = len(psutil.pids())
    return cpu_usage, memory_usage, disk_usage, process_count

def write_to_file(info):
    with open("system_log.txt", "a") as log_file:
        timestamp = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        log_file.write(f"{timestamp} - CPU: {info[0]}%, Memory: {info[1]}%, Disk:{info[2]}%, Processes: {info[3]}\n")

info = get_system_info()
write_to_file(info)
