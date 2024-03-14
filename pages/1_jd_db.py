import streamlit as st
import requests
from dotenv import load_dotenv
import os

load_dotenv()

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

with st.form(key='my_form'):
    st.write("Fill in the form to add a new job description")
    position_applied_for = st.text_input('Position Applied For')
    jd_file = st.file_uploader('Upload Job Description With txt file', type=['txt'])

    submit_button = st.form_submit_button('Submit')

    if submit_button:
        if not position_applied_for or not jd_file:
            st.error("Please fill in all fields")
        else:
            response = add_jd(position_applied_for, jd_file)
            st.write(response)
            
#show all job description
st.header("All job descriptions")
data = show_all_jd()
if data:
    for jd in data:
        st.header(jd['position_applied_for'])
        st.subheader("Job description")
        st.write(jd['jd_text'])
        st.subheader("Public date")
        st.write(jd['created_at'])
        st.markdown("***")
else:
    st.error("Error retrieving job descriptions")
# response = requests.get(f"{BACKEND_URL_API}/modules/crud_jds_router/", headers={"Content-Type": "application/json"})
# if response.status_code == 200:
#     data = response.json()
#     for jd in data:
#         st.header(jd['position_applied_for'])
#         st.subheader("Job description")
#         st.write(jd['jd_text'])
#         st.subheader("Public date")
#         st.write(jd['created_at'])
#         st.markdown("***")
# else:
#     st.error("Error retrieving job descriptions")
