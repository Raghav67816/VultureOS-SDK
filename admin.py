"""
admin.py
Project manager
Download SDK files
Setup apps
Create default .env file
"""
# Import dependencies
from requests import post
from typing import Optional
from configparser import ConfigParser

# Config object
config_obj = ConfigParser()

# Read config file
def read_config_file(section: str, key: str):
    data = config_obj.get(section, key)
    return data

# Update config file
def update_config_file(section: str, key: str, value: Optional[str], file_path: str = "config/settings.ini"):
    config_obj.set(section, key, value)
    with open(file_path, "w") as config_file:
        config_obj.write(config_file)
        config_file.flush()
        config_file.close()

# Create config file
def create_config_file(dir_path: str):
    print("Generating default configuration file.")
    config_obj.add_section("weather")
    config_obj.add_section("db")
    config_obj.add_section("user")
    config_obj.add_section("request_urls")
    config_obj.add_section("system")
    # Add data to sections - system
    config_obj.set("system", "ip_address", "")
    config_obj.set("system", "apps_path", "apps/")
    config_obj.set("system", "mqtt_port", "1883")
    # Add data to sections - weather
    config_obj.set("weather", "base_url", "https://api.openweathermap.org/data/2.5/weather?q=")
    config_obj.set("weather", "api_key", "sample api key")
    config_obj.set("weather", "city", "")
    # Add data to sections - db
    config_obj.set("db", "url", "mongodb://127.0.0.1:27017/")
    config_obj.set("db", "name", "Vulture_Web_DB")
    # Add data to sections - user
    config_obj.set("user", "display_name", "")
    config_obj.set("user", "id_token", "")
    config_obj.set("user", "user_uid", "")
    config_obj.set("user", "email", "")
    # Add data to section - request_urls
    config_obj.set("request_urls", "login", "http://127.0.0.1:8000/auth/login")
    config_obj.set("request_urls", "device_reg", "http://127.0.0.1:8000/devices/register")
    config_obj.set("request_urls", "get_app", "http://127.0.0.1:8000/vstore/get_apps")
    config_obj.set("request_urls", "upload_new", "http://127.0.0.1:8000/vstore/upload_new")

    try:
        with open(f"{dir_path}/settings.ini", "w") as settings_file:
            config_obj.write(settings_file)
            settings_file.flush()
            settings_file.close()
            print("File generated")

    except Exception as path_error:
        return path_error

# Authenticate user
def authenticate_user(email: str, password: str):
    auth_req_url = read_config_file("request_urls", "login")
    payload = {
        "email": email,
        "password": password
    }
    req = post(auth_req_url, json=payload)
    req_json = req.json()
    print("display name", req_json['displayName'])
    update_config_file("user", "display_name", req_json['displayName'])
    update_config_file("user", "id_token", req_json['idToken'])
    update_config_file("user", "user_uid", req_json['localId'])
    update_config_file("user", "email", req_json['email'])
