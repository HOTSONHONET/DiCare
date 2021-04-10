Skip to content
Search or jump to…

Pull requests
Issues
Marketplace
Explore
 
@HOTSONHONET 
HOTSONHONET
/
Crio_Task
1
00
Code
Issues
Pull requests
Actions
Projects
Wiki
Security
Insights
Settings
Crio_Task/install.sh
@HOTSONHONET
HOTSONHONET Initial Commit
Latest commit b10e259 on Feb 22
 History
 1 contributor
24 lines (14 sloc)  589 Bytes
  
#!/bin/bash


# Any installation related commands
sudo apt-get -y update
sudo apt-get -y install postgresql postgresql-contrib




# To install pip3 and install the dependecies
sudo apt-get install -y python3.7
sudo apt install -y python3-pip
sudo apt-get install -y libpq-dev
sudo apt-get install -y libmysqlclient-dev python-dev
pip3 install -r requirements.txt

# To set the password of postgresql db and create a database
sudo -u postgres psql -c "ALTER USER postgres WITH PASSWORD 'postgres';"
sudo -u postgres psql -c "CREATE DATABASE Patient;"



