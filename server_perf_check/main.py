import psutil
import platform
import datetime
import os

def bytes_to_gb(bytes_val):
    return round(bytes_val / (1024 ** 3), 2)

def get_system_info():
    print("="*30, "System Information", "="*30)
    print(f"System: {platform.system()} {platform.release()}")
    print(f"HostName: {platform.machine()}")
    print(f"Processor: {platform.processor()}")
    print(f"Uptime: {datetime.datetime.now() - datetime.datetime.fromtimestamp(psutil.boot_time())}")

def get_cpu_info():
    print("/n", "="*30, "CPU Info", "="*30)
    print(f"Logical cores: {psutil.cpu_count(logical=True)}")
    print(f"Physical cores: {psutil.cpu_count(logical=False)}")
    print(f"CPU Usage per core: {psutil.cpu_percent(percpu=True, interval=1)}")
    print(f"Total CPU Usage: {psutil.cpu_percent()}%")

def get_memory_info():
    print("/n", "="*30, "Disk Usage", "="*30)
    memory = psutil.virtual_memory()
    print(f"Total: {bytes_to_gb(memory.total)}GB")
    print(f"Available: {bytes_to_gb(memory.available)}GB")
    print(f"Used: {bytes_to_gb(memory.used)} GB ({memory.percent}%)")

def get_disk_info():
    print("/n", "="*30, "Disk Usage", "="*30)
    for partition in psutil.disk_partitions():
        usage = psutil.disk_usage(partition.mountpoint)
        print(f"{partition.device} - {partition.mountpoint} - {usage.percent}% used ({bytes_to_gb(usage.used)}GB/{bytes_to_gb(usage.total)}GB)")

def get_network_info():
    print(f"Server Perfomance Report - {datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S')}")
    net = psutil.net_io_counters()
    print(f"Bytes Sent: {bytes_to_gb(net.bytes_sent)} GB")
    print(f"Bytes Received: {bytes_to_gb((net.bytes_recv))} GB")

def main():
    print(f"Server Perfomance Report - {datetime.datetime.now().strftime('%Y-%m-%d &H:%M:%S')}")
    get_system_info()
    get_cpu_info()
    get_memory_info()
    get_disk_info()
    get_network_info()
    print("\n Analysis Complete. \n")

if __name__ == "__main__":
    main()
