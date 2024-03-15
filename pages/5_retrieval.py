import streamlit as st
import requests
from utils.retrieval import get_info_jd, get_jd, get_text_jd, slice_id, retrieve_test
from dotenv import load_dotenv
import os

st.set_page_config(page_title="Question Retrieval")

load_dotenv()

os.environ["BACKEND_URL_API"] = os.getenv("BACKEND_URL_API")
os.environ["FIREBASE_URL_STORAGEBUCKET"] = os.getenv("FIREBASE_URL_STORAGEBUCKET")
BACKEND_URL_API = os.environ.get("BACKEND_URL_API")
FIREBASE_URL_STORAGEBUCKET = os.environ.get("FIREBASE_URL_STORAGEBUCKET")

# Set up the title and introduction of the web app
st.header('Question Retrieval', divider="rainbow")

# Fetch JDs when the app loads
jds = get_jd()

id_jd = None

# Displaying the fetched JDs
jd_options = get_info_jd(jds)
jd_selected = st.selectbox('Select a JD:', jd_options, index=None)

# Button to display selected JD
# if st.button('Display Selected JD') :
if jd_selected is not None:
    # Extract the ID from the selected option
    id_jd = slice_id(jd_selected)

    # Get the text of the selected JD
    jd_text = get_text_jd(jds, id_jd)

    # Display the selected JD ID, position, and text
    st.info(f"You selected: {jd_selected}")
    with st.expander('Preview'):
        st.write(jd_text)

if id_jd is not None:
    result = retrieve_test(id_jd)
    question_tests_url = result.get("result")[0].get("question_tests_url")
    match_score = result.get("result")[0].get("match_score")
    st.success("Test Retrieval Completed")
    st.metric("Match Score", f"{(match_score*100):.2f} %")
    if st.button(f"Prepare to Download Test", key=question_tests_url, type="secondary"):
        url_download = f"{BACKEND_URL_API}/modules/download_file_gs_link?gs_link={question_tests_url}"
        response = requests.get(url_download)
        # Get the blob name from the gs link
        file_name = question_tests_url.split(f"{FIREBASE_URL_STORAGEBUCKET}/")[1]
        # Ensure response is successful
        if response.status_code == 200:
            st.download_button(label="Click here to download", data=response.content, file_name=file_name)
        else:
            st.error(f"Error downloading file: {response.status_code}")
