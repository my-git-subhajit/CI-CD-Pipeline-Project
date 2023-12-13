#!/bin/bash
PROJECT_DIR="CI-CD-Pipeline-Project"
cd  "$PROJECT_DIR"
# clone the new commit to that directory 
git pull origin main
cd 

sudo cp CI-CD-Pipeline-Project/* /var/www/html

sudo systemctl restart nginx

echo "Deployment successfully completed."