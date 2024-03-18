import psutil
import datetime
import operator

def get_system_info():
    try:
        cpu_usage = psutil.cpu_percent(interval=1)
        memory_usage = psutil.virtual_memory().percent
        disk_usage = psutil.disk_usage('/').percent
        process_count = len(psutil.pids())
        return cpu_usage, memory_usage, disk_usage, process_count
    except Exception as e:
        return f"Error getting system info: {e}"

def get_top_processes_by_cpu(n=5):
    processes = [(p.pid, p.info['name'], p.info['cpu_percent']) for p in psutil.process_iter(['name', 'cpu_percent'])]
    # Sort the list of tuples by CPU percent in descending order and return the top 'n' processes
    top_cpu_processes = sorted(processes, key=operator.itemgetter(2), reverse=True)[:n]
    return top_cpu_processes

def get_top_processes_by_memory(n=5):
    processes = [(p.pid, p.info['name'], p.info['memory_percent']) for p in psutil.process_iter(['name', 'memory_percent'])]
    # Sort the list of tuples by memory percent in descending order and return the top 'n' processes
    top_memory_processes = sorted(processes, key=operator.itemgetter(2), reverse=True)[:n]
    return top_memory_processes

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
    top_cpu = get_top_processes_by_cpu()
    top_memory = get_top_processes_by_memory()
    write_to_file(info)
    write_to_file(f"Top CPU Processes: {top_cpu}")
    write_to_file(f"Top Memory Processes: {top_memory}")
except Exception as e:
    print(f"An error occurred: {e}")
