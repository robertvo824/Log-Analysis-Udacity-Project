Logs Analysis Project
by Robert Vo
Logs Analysis Project, part of the Udacity Full Stack Web Developer Nanodegree.

Project purpose
To write SQL queries to answer the following questions about a PostgreSQL database containing the logs of a fictional newspaper website.

What are the most popular three articles of all time?
Who are the most popular article authors of all time?
On which days did more than 1% of requests lead to errors?
Required Libraries and Dependencies
The project code requires the following software:

Python 3.5.2
psycopg2 2.7.3.2
PostgreSQL 9.5.10
You can run the project in a Vagrant managed virtual machine (VM) which includes all the required dependencies (see below for how to run the VM). For this you will need Vagrant and VirtualBox software installed on your system.

Project contents
This project consists of the following files:

logs_analysis_tool.py - The Python program that connects to the PostgreSQL database, executes the SQL queries and displays the results.
newsdata.zip - A zip file containing a file that populates the news PostgreSQL database.
README.md - This read me file.
Vagrantfile - Configuration file for the Vagrant virtual machine.
How to Run the Project
Download the project zip file to your computer and unzip the file. Or clone this repository to your desktop.

Open the text-based interface for your operating system (e.g. the terminal window in Linux, the command prompt in Windows) and navigate to the project directory.

Bringing the VM up
Bring up the VM with the following command:

```vagrant up```
The first time you run this command, it will take awhile, as Vagrant needs to download the VM image.

You can then log into the VM with the following command:

```vagrant ssh```
More detailed instructions for installing the Vagrant VM can be found here.

Make sure you're in the right place
Once inside the VM, navigate to the tournament directory with this command:

```cd /vagrant```
Load the logs into the database
First, unzip the zip file with the command:

```unzip newsdata.zip```
Then run the following command to load the logs into the database:

```psql -d news -f newsdata.sql```
Running the reporting tool
The logs reporting tool is executed with the following command:

```python3 logs_analysis_tool.py```
The answers to the three questions should now be displayed.

Shutting the VM down
When you are finished with the VM, press Ctrl-D to log out of it and shut it down with this command:

```vagrant halt```
