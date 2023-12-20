import psutil

def check_cpu():
    cpu_usage = psutil.cpu_percent()
    return f"CPU usage: {cpu_usage}%"

def check_memory():
    memory_usage = psutil.virtual_memory().percent
    return f"Memory usage: {memory_usage}%"

def check_disk():
    disk_usage = psutil.disk_usage('/').percent
    return f"Disk usage: {disk_usage}%"

if __name__ == '__main__':
    print(check_cpu())
    print(check_memory())
    print(check_disk())

