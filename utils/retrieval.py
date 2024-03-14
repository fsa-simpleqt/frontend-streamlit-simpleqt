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

jd_option = st.selectbox(
    "Select a Job Description in the Database",
    get_info_jd(get_jd()),
    index=None,
    placeholder="Select a Job Description"
)

if jd_option is not None:
    id_jd = slice_id(jd_option)
    st.write(get_text_jd(get_jd(), id_jd))
else:
    st.info("Preview")