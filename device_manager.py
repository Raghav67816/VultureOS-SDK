"""
device manager.py
Add, update, remove devices from app
"""
# Import dependencies
from requests import post
from admin import read_config_file
from configparser import ConfigParser

device_config_obj = ConfigParser()

# Query devices
def query_device(collection_name: str, device_name: str, key: str):
    device_data = collection_name.find({"device name": device_name})
    if device_data is None:
        return None

    elif device_data is not None:
        return device_data[key]

# Validate device
def validate_device(device_name: str):
    device = query_device("devices", device_name, "device name")
    if device is None:
        return 1

    else:
        return 0

# Register new device
def register_new_device(device_type: str,
 device_sr_no: str, owner_uid: str, id_token: str):
    reg_request_url = read_config_file()

    req = post(reg_request_url, json={
        "device_type": device_type,
        "device_sr_no": device_sr_no,
        "id_token": id_token,
        "uid": owner_uid
    })
    print(req.text)

# Add device
def add_device(device_sr_no: str, device_name:str, device_type: str, topic_name: str):
    device_config_obj.add_section(device_sr_no)
    device_config_obj.set(device_name, "device_name", device_name)
    device_config_obj.set(device_name, "device_type", device_type)
    device_config_obj.set(device_name, "device_sr_no", device_sr_no)

    with open(f"devices/{device_name}.ini", "w") as device_file:
        device_config_obj.write(device_file)
        device_file.flush()
        device_file.close()
