import streamlit as st
import requests
import os

from dotenv import load_dotenv

load_dotenv()

os.environ["BACKEND_URL_API"] = os.getenv("BACKEND_URL_API")
BACKEND_URL_API = os.environ.get("BACKEND_URL_API")
test_url_route = f"{BACKEND_URL_API}/modules/crud_question_tests_router/"

def add_test(description, role, test_file):
    data = {"question_tests_role": role, 'question_tests_description':description}
    files = {"question_tests_url": test_file}
    response = requests.post(test_url_route, data=data, files=files)
    return response.json()

def show_all_test():
    response = requests.get(test_url_route, headers={"Content-Type": "application/json"})
    if response.status_code == 200:
        data = response.json()
        return data
    else:
        return None

def delete_test(test_id):
    response = requests.delete(f"{test_url_route}{test_id}")
    return response.json()
    
with st.container():
    st.header("Add Tests", divider="rainbow")
    with st.form(key='my_form'):
        st.write("Fill in the form to add a new Test")
        description = st.text_input('Description')
        role = st.text_input('Role')
        test_file = st.file_uploader('Upload Test With .json file', type=['json'])

        submit_button = st.form_submit_button('Submit')

        if submit_button:
            if not description or not role or not test_file:
                st.error("Please fill in all fields")
            else:
                result = add_test(description, role, test_file)
                if "message" in result:
                    st.success(result["message"])
                else:
                    st.error(result["message"])
            
with st.container():
    #show all Tests
    st.header("All Test", divider="rainbow")
    data = show_all_test()
    if data:
        for test in data:
            with st.expander(f"{test['question_tests_description']} - {test['question_tests_role']}", expanded=False):
                # download file to local

                # add delete button
                if st.button(f"Delete test {test['id']}"):
                    result_delete = delete_test(test['id'])
                    if "message" in result_delete:
                        st.success(result_delete["message"])
    else:
        st.error("Error retrieving tests")