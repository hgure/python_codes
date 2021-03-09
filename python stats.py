import psutil

cpu_stats = psutil.cpu_stats();
print(cpu_stats)

disk_usage = psutil.disk_usage('C:/')
print(disk_usage)