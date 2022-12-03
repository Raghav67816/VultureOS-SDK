"""
utils.py
Utility functions for system related operations
"""

import netifaces
from admin import config_obj
from pymongo.errors import PyMongoError
from pymongo.mongo_client import MongoClient

# Connect to db
def connect_to_db():
    db_url = config_obj.get("db", "url")
    db_name = config_obj.get("db", "name")
    
    try:
        client = MongoClient(db_url)
        parent_db = client[db_name]
        return parent_db

    except PyMongoError as db_error:
        return db_error

apps_collection = connect_to_db()["apps"]
devices_collection = connect_to_db()["devices"]

# Add new app
def app_new_app(app_name: str, app_path: str):
    try:
        app_payload = {
            "app name": app_name,
            "removable": True,
            "app path": app_path
        }

        apps_collection.insert_one(app_payload)

    except Exception as db_error:
        return db_error

# Get ip address
def get_ip_address():
    addr_raw = netifaces.ifaddresses('wlo1')
    addr_dict = addr_raw[netifaces.AF_INET]
    addr = addr_dict.get('addr')
    return addr
