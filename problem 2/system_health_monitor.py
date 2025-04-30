import psutil
import time
import logging
import os
from datetime import datetime

# Thresholds
CPU_THRESHOLD = 80  # in percentage
MEMORY_THRESHOLD = 80  # in percentage
DISK_THRESHOLD = 80  # in percentage
PROCESS_COUNT_THRESHOLD = 2000  # arbitrary threshold for processes


LOG_FILE = "system_health_monitor.log"

# Ensure log file exists
if not os.path.exists(LOG_FILE):
    with open(LOG_FILE, 'w') as f:
        f.write("System Health Monitor Log File Created\n")

# Logging setup
logging.basicConfig(
    filename=LOG_FILE,
    level=logging.INFO,
    format="%(asctime)s - %(levelname)s - %(message)s"
)

def log_and_alert(metric_name, value, threshold):
    msg = f"{metric_name} usage: {value:.2f}%"
    if value > threshold:
        alert_msg = f"ALERT: {metric_name} exceeded threshold! ({value:.2f}% > {threshold}%)"
        print(alert_msg)
        logging.warning(alert_msg)
    else:
        logging.info(msg)

def check_system_health():
    # CPU
    cpu = psutil.cpu_percent(interval=1)
    log_and_alert("CPU", cpu, CPU_THRESHOLD)

    # Memory
    memory = psutil.virtual_memory().percent
    log_and_alert("Memory", memory, MEMORY_THRESHOLD)

    # Disk
    disk = psutil.disk_usage('/').percent
    log_and_alert("Disk", disk, DISK_THRESHOLD)

    # Process count
    process_count = len(psutil.pids())
    if process_count > PROCESS_COUNT_THRESHOLD:
        alert_msg = f"ALERT: Process count exceeded! ({process_count} > {PROCESS_COUNT_THRESHOLD})"
        print(alert_msg)
        logging.warning(alert_msg)
    else:
        logging.info(f"Running processes: {process_count}")

def monitor_system(interval_sec=5):
    logging.info("System health monitoring started.")
    while True:
        check_system_health()
        time.sleep(interval_sec)

if __name__ == "__main__":
    monitor_system()