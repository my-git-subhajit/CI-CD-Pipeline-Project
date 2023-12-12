import requests

def get_commits(repo_url):
    response = requests.get(repo_url)
    
    if response.status_code == 200:
        commits = response.json()
        return commits
    else:
        print(f"Failed to get commits. Status code: {response.status_code}")
        print(f"Response content: {response.content}")
        raise Exception("Could not get commits")

def main():
    repo_url = "https://api.github.com/repos/my-git-subhajit/CI-CD-Pipeline-Project/commits"
    
    # Get the latest commits.
    try:
        commits = get_commits(repo_url)
        sha_latest = str(commits[0]["sha"])
        print(sha_latest)
        # You can perform additional actions with the latest commit SHA here.
    except Exception as e:
        print(f"Error: {e}")
        print("No commits found or there was an issue fetching commits.")

if __name__ == "__main__":
    main()
