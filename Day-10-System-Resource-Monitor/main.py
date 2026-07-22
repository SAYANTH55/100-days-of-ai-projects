import psutil
import time
import os


def show_system_info():

    # CPU Usage
    cpu_usage = psutil.cpu_percent(interval=1)

    # Memory Information
    memory = psutil.virtual_memory()

    # Disk Information
    disk = psutil.disk_usage("C:\\")

    # Battery Information
    battery = psutil.sensors_battery()

    # Network Information
    network = psutil.net_io_counters()
    os.system("cls")

    print("\n================ SYSTEM RESOURCE MONITOR ================\n")

    # CPU
    print(f"CPU Usage          : {cpu_usage}%")

    # RAM
    print(f"RAM Usage          : {memory.percent}%")
    print(f"Total RAM          : {round(memory.total / (1024**3), 2)} GB")
    print(f"Available RAM      : {round(memory.available / (1024**3), 2)} GB")

    print()

    # Disk
    print(f"Disk Usage         : {disk.percent}%")
    print(f"Total Disk         : {round(disk.total / (1024**3), 2)} GB")
    print(f"Used Disk          : {round(disk.used / (1024**3), 2)} GB")
    print(f"Free Disk          : {round(disk.free / (1024**3), 2)} GB")

    print()

    # Battery
    if battery:
        print(f"Battery Percentage : {battery.percent}%")

        if battery.power_plugged:
            print("Charging Status    : Charging")
        else:
            print("Charging Status    : Not Charging")
    else:
        print("Battery Information: Not Available")

    print()

    # CPU Cores
    print(f"Physical CPU Cores : {psutil.cpu_count(logical=False)}")
    print(f"Logical CPU Cores  : {psutil.cpu_count(logical=True)}")

    print()

    # Network
    print(f"Data Sent          : {round(network.bytes_sent / (1024**2), 2)} MB")
    print(f"Data Received      : {round(network.bytes_recv / (1024**2), 2)} MB")


while True:

    show_system_info()

    time.sleep(2)