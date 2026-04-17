import os
import json
import time

def get_metrics():
    # Get CPU Load
    load = os.getloadavg()[0]
    cpu_perc = round((load / 2) * 100, 2) # t3.micro has 2 vCPUs
    
    # Get Memory Usage
    mem = os.popen('free -m').readlines()
    mem_total = int(mem[1].split()[1])
    mem_used = int(mem[1].split()[2])
    mem_perc = round((mem_used / mem_total) * 100, 2)

    data = {
        "cpu": cpu_perc,
        "memory": mem_perc,
        "status": "ONLINE",
        "last_update": time.strftime('%H:%M:%S')
    }
    
    # Write to the web directory
    with open('/var/www/hem-cloud/dist/sys_data.json', 'w') as f:
        json.dump(data, f)

while True:
    get_metrics()
    time.sleep(5) # Updates every 5 seconds
