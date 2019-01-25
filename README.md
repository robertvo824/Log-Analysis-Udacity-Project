# Logs Analysis Project
### By Robert Vo<br><br>

## Objective
Build an internal reporting tool that will use information from a news database to discover and answer the following three questions:
1. What are the most popular three articles of all time? 
2. Who are the most popular article authors of all time?
3. On which days did more than 1% of requests lead to errors?

### Required Skills<br>
* Relational Datasbases
* SQL
* Python

### Tools Preparation<br>
1. Install [Vagrant](https://www.vagrantup.com/) and 
2. Install [VirtualBox](https://www.virtualbox.org/)<br>
3. Download or clone from Github the necessary setup files from [fullstack-nandegree-vm repository](https://github.com/udacity/fullstack-nanodegree-vm)</br>
4. Download the database setup file - [Download data here](https://d17h27t6h515a5.cloudfront.net/topher/2016/August/57b5f748_newsdata/newsdata.zip)
5. Unzip the file after downloading it.
6. Find the file, newsdata.sql, and put it into the vagrant directory which is shared with your virtual machine
7. Download this reporting tool - [Logs Analysis Tool]
8. Copy the files into the vagrant directory

### Start the VM<br>
1. Change  your current working directory to vagrant directory.<br>
2. Open Terminal and run `vagrant up` to build the VM.<br>
3. Run `vagrant ssh` to log in and connect to the VM.<br>
4. Once you're in vagrant, run `cd /vagrant` to change the directory to the vagrant directory.<br>
5. Run command `psql -d news -f newsdata.sql` to load the database<br>
6. Use command `python logs_analysis.py` to run the programm<br>
