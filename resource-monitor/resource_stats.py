import psutil
logical = psutil.cpu_count(logical=True)  # Returns the number of logical CPUs in the system
physical = psutil.cpu_count(logical=False)  # Returns the number of physical CPUs in the system
cpu_percent = psutil.cpu_percent(interval=1,percpu=False)  # Returns the CPU utilization percentage over a 1-second interval
print(f"Logical CPUs : {logical}")
print(f"Physical CPUs: {physical}")
print(f"CPU Percent  : {cpu_percent}%")