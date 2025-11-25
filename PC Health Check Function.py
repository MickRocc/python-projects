def pc_health():
  import shutil
  import psutil
  disk_usage = shutil.disk_usage("/")
  print("Disk Usage:",disk_usage)
  # Output will show total, used, and free space in bytes on the root filesystem.
  ram = psutil.virtual_memory()
  print("RAM Usage:", ram)
  # Output will show total, available, percent used, and other memory details.
  cpu_usage = psutil.cpu_percent(interval=0.1)
  print("CPU Usage:", cpu_usage)
  # Output will show the CPU usage percentage over a 0.1 second interval.

pc_health()

