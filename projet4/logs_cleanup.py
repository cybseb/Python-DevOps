import os
import time

def cleanup_logs(directory, days):
    now = time.time()
    cutoff = now - (days * 86400)
    for filename in os.listdir(directory):
        path = os.path.join(directory, filename)
        if os.path.isfile(path) and os.stat(path).st_mtime < cutoff:
            os.remove(path)

if __name__ == '__main__':
    directory = '/var/log'
    days = 10
    cleanup_logs(directory, days)
