'''

# pip install psutil
# pip install py-notifier
# pip install win10toast

'''
import psutil
from pynotifier import Notification

battery = psutil.sensors_battery()
plugged = battery.power_plugged
percent = battery.percent

if percent >= 30:
    Notification(
        title="Battery Low",
        description=str(percent) + "% Battery remain!!",