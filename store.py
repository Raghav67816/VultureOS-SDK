"""
store.py
Vulture store functions
"""
from wget import download
from requests import post
from admin import config_obj
from json import dumps, loads

# Get apps
def get_apps():
    get_app_req_url = config_obj.get("request_urls", "get_app")
    req = post(get_app_req_url)
    req_response = req.json()
    dict_req = dumps(req_response)
    print(dict_req, type(dict_req))

# Download app
def download_app(repo_path: str, app_name: str):
    try:
        download_path = config_obj.get("system", "apps_path")
        download(repo_path, f"{download_path}{app_name}")
        app_details = {
                "app name": app_name,
                "path": f"{download_path}{app_name}",
                "removable": True,
        }

        with open("config/installed_apps.json", "w") as apps_file:
            data = apps_file.read()
            data_dict = loads(data)
            data_dict.update(app_details)
            dumps(data_dict)
            apps_file.close()

    except Exception as download_error:
        return download_error
