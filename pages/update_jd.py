import streamlit as st
import requests

url_upload = "https://tony2802-fsa-simpleqt.hf.space/modules/crud_jds_router/?position_applied_for=%C4%91awad"

with st.form(key='my_form'):
    st.write("Fill in the form to add a new job description")
    position_applied_for = st.text_input(label='Position')
    jd_file = st.file_uploader(label='Upload Job Description', type=['txt', 'docx', 'pdf'])

    submit_button = st.form_submit_button(label='Submit')

    if submit_button:
        if jd_file is not None:
            jd_text = jd_file.read().decode()
            payload = {
                "position_applied_for": position_applied_for,
                "jd_text": jd_text,
            }
            response = requests.post(url_upload, headers={"Content-Type": "application/json"}, json=payload)

            if response.status_code == 200:
                st.success("Job description added successfully")
            else:
                st.error(f"Error adding job description: {response.status_code}")
        else:
            st.error("Please upload a job description file")


