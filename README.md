# MongoDB Atlas Backup Script

This script is designed to take backups of MongoDB databases running on MongoDB Atlas. It utilizes the `mongodump` command-line tool to create backups in BSON format.

## Prerequisites

Before using this script, make sure you have the following:

- Python 3 installed
- `pymongo` library installed (you can install it using `pip install pymongo`)
- `mongodump` command-line tool installed (usually bundled with MongoDB)

## Configuration

Before running the script, you need to provide the necessary configuration. Open the script file (`mongodb_backup.py`) and update the following variables:

- `atlas_connection_string`: The connection string for your MongoDB Atlas cluster.
- `atlas_cluster_name`: The name of your MongoDB Atlas cluster.
- `backup_parent_folder`: The path to the parent folder where backup folders will be created.

## Usage

To run the script, execute the following command:

python mongodb_backup.py



The script will connect to MongoDB Atlas, retrieve the list of databases (excluding the 'admin' database), and create a backup file for each database in a folder named after the current date. The backup files will be saved in the specified `backup_parent_folder`.

## Schedule Backup

To schedule the script to run automatically at the end of the day, you can use a task scheduler or a cron job depending on your operating system. Refer to the documentation or search online for instructions on how to schedule tasks on your specific platform.
For example, on Unix-like systems, you can use cron to schedule the script to run at 11:59 PM every day. Here's an example cron job entry:

`59 23 * * * python /path/to/mongodb_backup.py`

Adjust the path to the script file as per your setup.

## Customization
- To exclude specific databases from the backup process, you can modify the `database_names` list in the script to exclude the desired databases.
- If you want to change the backup file format or customize the backup options, you can modify the `mongodump` command arguments in the script.
