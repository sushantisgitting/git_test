import subprocess
import shutil
import os
import stat

def on_rm_error(func, path, exc_info):
    try:
        os.chmod(path, stat.S_IWRITE)
        func(path)
    except Exception:
        pass

repos = {
    "student-management-app": {
        "lang": "Java",
        "file": "Booster.java",
        "template": "public class Booster {\n\tpublic static void main(String[] args) {\n\t\tString s = \"This is a Java booster file to increase language diversity. {i}\";\n\t}\n}\n"
    },
    "cncommands": {
        "lang": "Kotlin",
        "file": "booster.kt",
        "template": "fun main() {\n\tval s = \"This is a Kotlin booster file to increase language diversity. {i}\"\n}\n"
    }
}

temp_dir = "temp_boost"
os.makedirs(temp_dir, exist_ok=True)

for repo_name, config in repos.items():
    print(f"\n--- Processing {repo_name} for {config['lang']} ---")
    clone_url = f"https://github.com/sushantisgitting/{repo_name}.git"
    target_path = os.path.join(temp_dir, repo_name)
    
    # Clean previous clone if exists
    if os.path.exists(target_path):
        shutil.rmtree(target_path, onerror=on_rm_error)
        
    # Clone repository
    try:
        subprocess.run(["git", "clone", clone_url, target_path], check=True)
    except subprocess.CalledProcessError as e:
        print(f"Failed to clone {repo_name}: {e}")
        continue
        
    # Create 50KB file
    file_path = os.path.join(target_path, config['file'])
    content = ""
    for i in range(600):
        content += config['template'].replace("{i}", str(i))
        
    with open(file_path, "w") as f:
        f.write(content)
        
    # Stage, Commit, Push
    env = os.environ.copy()
    env["GIT_AUTHOR_NAME"] = "sushantisgitting"
    env["GIT_AUTHOR_EMAIL"] = "pvsksushant@gmail.com"
    env["GIT_COMMITTER_NAME"] = "sushantisgitting"
    env["GIT_COMMITTER_EMAIL"] = "pvsksushant@gmail.com"
    
    try:
        subprocess.run(["git", "-C", target_path, "add", config['file']], check=True)
        subprocess.run(["git", "-C", target_path, "commit", "-m", f"feat: boost {config['lang']} language statistics"], env=env, check=True)
        
        # Try pushing to main first
        try:
            subprocess.run(["git", "-C", target_path, "push", "origin", "main"], check=True)
            print(f"Successfully pushed {config['lang']} boost to {repo_name} (main)!")
        except subprocess.CalledProcessError:
            print("Failed to push to main. Retrying push with master branch...")
            subprocess.run(["git", "-C", target_path, "push", "origin", "master"], check=True)
            print(f"Successfully pushed {config['lang']} boost to {repo_name} (master)!")
            
    except subprocess.CalledProcessError as e:
        print(f"Failed to commit/push for {repo_name}: {e}")

# Cleanup temp folder
shutil.rmtree(temp_dir, onerror=on_rm_error)
print("\nCompleted language boosting utility execution!")
