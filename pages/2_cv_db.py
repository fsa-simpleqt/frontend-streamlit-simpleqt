import streamlit as st
import requests
import os
import base64

from utils.match_utils import get_jd, get_info_jd, slice_id
from dotenv import load_dotenv

load_dotenv()

os.environ["BACKEND_URL_API"] = os.getenv("BACKEND_URL_API")
os.environ["FIREBASE_URL_STORAGEBUCKET"] = os.getenv("FIREBASE_URL_STORAGEBUCKET")
BACKEND_URL_API = os.environ.get("BACKEND_URL_API")
FIREBASE_URL_STORAGEBUCKET = os.environ.get("FIREBASE_URL_STORAGEBUCKET")

cv_url_route = f"{BACKEND_URL_API}/modules/crud_cvs_router/"

def add_cv(name_candidate, apply_jd_id, cv_file):
    data = {'name_candidate':name_candidate,"apply_jd_id": apply_jd_id}
    files = {"file_cv": cv_file}
    response = requests.post(cv_url_route, data=data, files=files)
    return response.json()

def show_all_cv():
    response = requests.get(cv_url_route, headers={"Content-Type": "application/json"})
    if response.status_code == 200:
        data = response.json()
        return data
    else:
        return None

def delete_user(cv_id):
    # Gửi yêu cầu DELETE đến API để xóa người dùng
    response = requests.delete(f"{cv_url_route}{cv_id}")
    return response.json()
    
with st.container():
    st.header("Add CVs", divider="rainbow")
    with st.form(key='my_form'):
        st.write("Fill in the form to add a new CV")
        name_candidate = st.text_input('Name Candidate')
        apply_jd_info = st.selectbox(
            "Select a Job Description from the Database",
            get_info_jd(get_jd()),
            index=None,
            placeholder="Select a Job Description"
        )

        cv_file = st.file_uploader('Upload CV With .docx and .pdf file', type=['docx', 'pdf'])

        submit_button = st.form_submit_button('Submit')

        if submit_button:
            apply_jd_id = slice_id(apply_jd_info)
            if not name_candidate or not apply_jd_id or not cv_file:
                st.error("Please fill in all fields")
            else:
                result = add_cv(name_candidate, apply_jd_id, cv_file)
                if "message" in result:
                    st.success(result["message"])
                else:
                    st.error(result["message"])
            
with st.container():
    #show all CV
    st.header("All CVs", divider="rainbow")
    data = show_all_cv()
    if data:
        for cv in data:
            with st.expander(f"{cv['name_candidate']} - {cv['apply_position']}", expanded=False):
                # Download file to local
                if st.button(f"Download CV", key=cv["id_cv"], type="secondary"):
                    url_download = f"{BACKEND_URL_API}/modules/download_file_gs_link?gs_link={cv['cv_url']}"
                    response = requests.get(url_download)
                    # Get the blob name from the gs link
                    file_name = cv['cv_url'].split(f"gs://{FIREBASE_URL_STORAGEBUCKET}/")[1]
                    # Ensure response is successful
                    if response.status_code == 200:
                        st.download_button(label="Click here to download", data=response.content, file_name=file_name)
                    else:
                        st.error(f"Error downloading file: {response.status_code}")
                if st.button(f"Delete CV - {cv['id_cv']}", type="primary"):
                    result_delete = delete_user(cv['id_cv'])
                    if "message" in result_delete:
                        st.success(result_delete["message"])
                        # refresh the page
                        st.rerun()
    else:
        st.error("Error retrieving CVs")
