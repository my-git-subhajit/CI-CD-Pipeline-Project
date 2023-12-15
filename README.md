# CI-CD-Pipeline-Project
Creating CI-CD Pipeline Project  which will monitor all the code changes made in an HTML website,  codes committed on GitHub using python bash sh script, python code script, and cron job

•	Task 1: Set Up a Simple HTML Project 
	Create a simple HTML project and push it to a GitHub repository. 
•	Task 2: Set Up an AWS EC2/Local Linux Instance with Nginx
•	Task 3: Write a Python Script to Check for New Commits
	 Create a Python script to check for new commits using the GitHub API.
•	Task 4: Write a Bash Script to Deploy the Code
	Create a bash script to clone the latest code and restart Nginx.
•	Task 5: Set Up a Cron Job to Run the Python Script
	Create a cron job to run the Python script at regular intervals.
•	Task 6: Test the Setup 
	Make a new commit to the GitHub repository and check that the changes are automatically deployed. 

Task 1:  Simple HTML File index.html

<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Important HTML Project</title>
</head>
<body>
    <h1>Hello, GitHub!</h1>
    <p>This web page is used for demo purpose to check CI-CD pipeline works fine or not</p>
    <h2>cron job is working fine</h2>
    <h2>We are good now.</h2>
    <h2>It should be good now.</h2>
    
</body>
</html>

Task 2: Write a Python script to connect with GitHub API and track the new changes committed to GitHub.
It includes code changes in HTML file and push the new code or updated HTML file to GitHub. 
!! Make sure your GitHub repository is public !!


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

    if commits: 
        sha_latest = str(commits[0]["sha"])
    # sha1_latest= str(commits[1]["sha"])

    if sha_latest:
        subprocess.call(['sh', '/home/ubuntu/deploy.sh'])
        #print (sha_latest)
        #print(sha_remote)
    else:
        print("No Commits found.")
    

if __name__ == "__main__":
    main()
Task 3: Create an AMAZON EC2 Instance linux machine and install nginx web server on that machine.

Task 4 – Write a bash script to deploy latest code  and new commits on GitHub.
 deploy.sh script will be run on EC2 Linux instance and deploy new commits or code changes in index.html file on github.
How it works?
It will pull the latest commits changes from GitHub, deploy those new changes on EC2 Instance Nginx server and restart nginx server on that EC2 instance.
Linux Command:  sudo systemctl restart nginx

#!/bin/bash
PROJECT_DIR="CI-CD-Pipeline-Project"
cd  "$PROJECT_DIR"
# clone the new commit to that directory 
git pull origin main
cd 

sudo cp CI-CD-Pipeline-Project/* /var/www/html

sudo systemctl restart nginx

echo "Deployment successfully completed."

Running deploy.sh script on EC2 Nginx Server.
./deploy.sh or bash deploy.sh

Task 5 – Set up a Cron Job to run the Python script  at regular intervals on the EC2 instance nginx server.

Created script.sh file in order to configure with cron job and run that script  by command 
bash script.sh
•	Ensure you  are running command as sudo su (super user)

#!/bin/bash

cd CI-CD-Pipeline-Project

python3 CheckCommitsGit.py


