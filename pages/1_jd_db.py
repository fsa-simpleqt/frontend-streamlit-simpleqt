import streamlit as st
import requests
import os
import pandas as pd

from dotenv import load_dotenv

load_dotenv()

st.set_page_config(page_title="Job Description Database")

os.environ["BACKEND_URL_API"] = os.getenv("BACKEND_URL_API")
BACKEND_URL_API = os.environ.get("BACKEND_URL_API")

def add_jd(position_applied_for, file_jd):
    url = f"{BACKEND_URL_API}/modules/crud_jds_router/"
    data = {"position_applied_for": position_applied_for}
    files = {"file_jd": file_jd}
    response = requests.post(url, data=data, files=files)
    return response.json()

def show_all_jd():
    url = f"{BACKEND_URL_API}/modules/crud_jds_router/"
    response = requests.get(url, headers={"Content-Type": "application/json"})
    if response.status_code == 200:
        data = response.json()
        return data
    else:
        return None

def delete_user(user_id):
    # Send DELETE request to API to delete the user
    response = requests.delete(f"{BACKEND_URL_API}/modules/crud_jds_router/{user_id}")
    return response.json()
    
with st.container():
    st.header("Add job descriptions", divider="rainbow")
    with st.form(key='my_form'):
        st.write("Fill in the form to add a new job description")
        position_applied_for = st.text_input('Position Applied For')
        jd_file = st.file_uploader('Upload Job Description With txt file', type=['txt'])

        submit_button = st.form_submit_button('Submit')

        if submit_button:
            if not position_applied_for or not jd_file:
                st.error("Please fill in all fields")
            else:
                result = add_jd(position_applied_for, jd_file)
                if "message" in result:
                    st.success(result["message"])
            
with st.container():
    #show all job description
    st.header("All job descriptions", divider="rainbow")
    data = show_all_jd()
    if data:
        for jd in data:
            with st.expander(f"{jd['position_applied_for']}", expanded=False):
                # add delete button
                if st.button(f"Delete JD {jd['id_jd']}"):
                    result_delete = delete_user(jd['id_jd'])
                    if "message" in result_delete:
                        st.success(result_delete["message"])
                        # refresh the page
                        st.rerun()
                st.write(f"JD Descriptions: {jd['jd_text']}")
    else:
        st.error("Error retrieving job descriptions")
