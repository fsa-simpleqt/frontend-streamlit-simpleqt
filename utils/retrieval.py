import re
import requests
import json
import streamlit as st

def get_jd():
    # Define the URL
    url = "https://tony2802-fsa-simpleqt.hf.space/modules/crud_jds_router/"
    # Send a GET request
    response = requests.get(url)
    # Check if the response is not empty
    if response.content.strip():
        # Print the response content
        return json.loads(response.content.decode("utf-8"))
    else:
        return None

def get_info_jd(jd_list):
    info_jd_list = [f"{jd.get("position_applied_for")} [{jd.get("id_jd")}]" for jd in jd_list]
    return info_jd_list

def slice_id(info: str):
    return re.search(r'\[(.*?)\]', info).group(1)

def get_text_jd(jd_list, id_jd):
    for jd in jd_list:
        if jd.get("id_jd") == id_jd:
            return jd.get("jd_text")
    return None

def retrieve_test(id_test):
    url = f"https://tony2802-fsa-simpleqt.hf.space/modules/qtretrieval/send_jd_to_get_question?id_jd={id_test}"
    response = requests.post(url)
    return json.loads(response.content.decode("utf-8"))

def download_test(url):
    response = requests.get(url)
    return response.content
