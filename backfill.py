import subprocess
import datetime
import random
import os

# Configuration
DAYS_TO_BACKFILL = 180
GIT_USER = "sushantisgitting"
GIT_EMAIL = "pvsksushant@gmail.com"
FILE_NAME = "backfill_history.txt"

print("Starting historical git commit generation...")

# Set Git Identity
subprocess.run(["git", "config", "user.name", GIT_USER], check=True)
subprocess.run(["git", "config", "user.email", GIT_EMAIL], check=True)

# Generate a list of dates
base = datetime.datetime.now()
date_list = [base - datetime.timedelta(days=x) for x in range(DAYS_TO_BACKFILL)]

total_commits = 0

# For each date, randomly decide how many commits to make
for date in date_list:
    # 25% chance of skipping the day to look natural
    if random.random() < 0.25:
        continue
        
    num_commits = random.randint(1, 3)
    for i in range(num_commits):
        # Generate random hour/minute/second
        hour = random.randint(9, 21)
        minute = random.randint(0, 59)
        second = random.randint(0, 59)
        commit_date = date.replace(hour=hour, minute=minute, second=second)
        
        # ISO 8601 format
        git_date = commit_date.strftime("%Y-%m-%dT%H:%M:%S")
        
        # Append to log file
        with open(FILE_NAME, "a") as f:
            f.write(f"Commit at {git_date}\n")
            
        # Git stage
        subprocess.run(["git", "add", FILE_NAME], check=True)
        
        # Set Git Date Environment variables
        env = os.environ.copy()
        env["GIT_AUTHOR_DATE"] = git_date
        env["GIT_COMMITTER_DATE"] = git_date
        
        # Commit
        subprocess.run(
            ["git", "commit", "-m", f"chore: archive system activity log for {git_date.split('T')[0]}"],
            env=env,
            stdout=subprocess.DEVNULL,
            stderr=subprocess.DEVNULL,
            check=True
        )
        total_commits += 1

print(f"Successfully generated {total_commits} historical commits locally!")
print("To push these to GitHub, run: git push origin main")
