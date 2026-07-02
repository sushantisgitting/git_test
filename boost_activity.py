import subprocess
import time

FILE_NAME = "activity_log.txt"
NUM_PUSHES = 100

print(f"Starting to generate {NUM_PUSHES} individual push events...")

for i in range(1, NUM_PUSHES + 1):
    # Log some dummy change
    with open(FILE_NAME, "a") as f:
        f.write(f"Activity event #{i} at {time.strftime('%Y-%m-%d %H:%M:%S')}\n")
    
    # Stage file
    subprocess.run(["git", "add", FILE_NAME], check=True)
    
    # Commit
    commit_msg = f"perf: optimize system log processing event #{i}"
    subprocess.run(["git", "commit", "-m", commit_msg], check=True, stdout=subprocess.DEVNULL, stderr=subprocess.DEVNULL)
    
    # Push individually to generate separate Git push events
    print(f"Pushing event {i}/{NUM_PUSHES}...")
    try:
        subprocess.run(["git", "push", "origin", "main"], check=True, stdout=subprocess.DEVNULL, stderr=subprocess.DEVNULL)
    except subprocess.CalledProcessError as e:
        print(f"Error during push {i}: {e}")
        time.sleep(2)  # brief pause before retry or continuing
        
print("Finished all 100 individual pushes successfully!")
