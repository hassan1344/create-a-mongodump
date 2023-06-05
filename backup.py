import datetime
import os
from pymongo import MongoClient
import subprocess

def generate_backup():

    atlas_connection_string =  "" #mongo atlas url (recommended : replace the username:password with the super DBA)

    backup_parent_folder = ""  #folder where backups will be placed. (eg : D:\\backup)

    timestamp = datetime.datetime.now()
    backup_folder = timestamp.strftime("%Y-%m-%d")    #Inside the parent folder, there will be a subfolder of each day (named with a timestamp)

    backup_path = os.path.join(backup_parent_folder, backup_folder)
    os.makedirs(backup_path, exist_ok=True)

    client = MongoClient(atlas_connection_string)
    database_names = client.list_database_names()
    database_names = [name for name in database_names if name!='admin' and name!='local']  

    for database_name in database_names:
        backup_file = os.path.join(backup_path, f"{database_name}")
        subprocess.run(["mongodump", "--uri", atlas_connection_string, "--out", backup_file, "--db", database_name])

    client.close()


generate_backup()