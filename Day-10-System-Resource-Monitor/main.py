import psutil

# CPU Usage
cpu_usage = psutil.cpu_percent(interval=1)

# Memory Information
memory = psutil.virtual_memory()

print("\n===== SYSTEM RESOURCE MONITOR =====\n")

print(f"CPU Usage: {cpu_usage}%")
print(f"RAM Usage: {memory.percent}%")
print(f"Total RAM: {round(memory.total / (1024**3), 2)} GB")
print(f"Available RAM: {round(memory.available / (1024**3), 2)} GB")