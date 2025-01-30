import schedule
import time
import subprocess
from datetime import datetime
import pytz

# Define the dates on which to run the script
dates = [
    "2025-02-11", "2025-03-11", "2025-04-10", "2025-05-12",
    "2025-06-12", "2025-07-11", "2025-08-12", "2025-09-12",
    "2025-10-09", "2025-11-10", "2025-12-09"
]

# Function to run the script
def run_script():
    subprocess.run(["python", "multi_agents/main.py"])

# Schedule the script on the specified dates at 12:00:10 PM Eastern Time
eastern = pytz.timezone('US/Eastern')
for date_str in dates:
    date = datetime.strptime(date_str, "%Y-%m-%d")
    schedule.every().day.at("12:00:10").do(run_script).tag(date_str)

while True:
    now = datetime.now(eastern)
    today = now.strftime("%Y-%m-%d")
    current_time = now.strftime("%H:%M:%S")
    if today in dates and current_time == "12:00:10":
        schedule.run_pending()
    time.sleep(1)  # Sleep for one second
