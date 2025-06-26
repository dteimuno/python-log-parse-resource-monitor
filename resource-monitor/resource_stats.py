import psutil
logical = psutil.cpu_count(logical=True)  # Returns the number of logical CPUs in the system
physical = psutil.cpu_count(logical=False)  # Returns the number of physical CPUs in the system
cpu_percent = psutil.cpu_percent(interval=1,percpu=False)  # Returns the CPU utilization percentage over a 1-second interval
memory = psutil.virtual_memory()  # Returns the virtual memory statistics
print(f"Logical CPUs : {logical}")
print(f"Physical CPUs: {physical}")
print(f"CPU Percent  : {cpu_percent}%")
print(f"Memory Total : {memory.total / (1024 ** 3):.2f} GB")

def get_memory_usage():
    """
    Returns the memory usage statistics.
    """
    memory = psutil.virtual_memory()
    return {
        'total': memory.total,
        'available': memory.available,
        'used': memory.used,
        'percent': memory.percent
    }