import requests
import json
import subprocess

def get_commits(repo_url):
    response = requests.get(repo_url)
    #check the commit
    if response.status_code == 200:
        commits = response.json()
        return commits
    else:
        raise Exception("Could not get commits")
    
def main():
    
    repo_url = "https://api.github.com/repos/my-git-subhajit/CI-CD-Pipeline-Project/commits"

    # Get the latest commits.
    commits = get_commits(repo_url)

    sha_latest = str(commits[0]["sha"])
    # sha1_latest= str(commits[1]["sha"])

    if sha_latest:
        subprocess.call(['sh', '/home/ubuntu/deploy.sh'])
        #print(sha_remote)
    else:
        print("Already up to date.")
    

if __name__ == "__main__":
    main()