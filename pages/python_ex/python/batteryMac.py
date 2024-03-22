# make sure you have installed psutil via pip3 install psutil!
import psutil
import time
import subprocess

# Function to display notification on macOS
def notify_mac(title, message):
    subprocess.call(['osascript', '-e', f'display notification "{message}" with title "{title}"'])

# Loop that checks if battery needs charging
while True:
    battery = psutil.sensors_battery()
    percent = battery.percent
    low = 10

    if percent > low:
            notify_mac("Battery", f"No charging needed! {percent}% Battery remaining.")

    else:
         notify_mac("Battery", f"Please charge, {percent}% Battery remaining.")

 # notify user every 60 min
    time.sleep(60 * 60)