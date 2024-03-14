import requests
import json
import re

def get_jd():
    # Define the URL
    url = "https://tony2802-fsa-simpleqt.hf.space/modules/crud_jds_router/"
    # Send a GET request
    response = requests.get(url)
    # Print the response content
    return json.loads(response.content.decode("utf-8"))

def get_info_jd(jd_list):
    info_jd_list = [f"{jd.get("position_applied_for")} [{jd.get("id_jd")}]" for jd in jd_list]
    return info_jd_list