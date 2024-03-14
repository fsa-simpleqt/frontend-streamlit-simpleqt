import streamlit as st
from utils.jd_utils import get_jd,get_info_jd

st.set_page_config(page_title="My Data", page_icon="📊")

jd_option = st.selectbox(
    "Select a Job Description in the Database",
    get_info_jd(get_jd()),
    index=None,
    placeholder="Select a Job Description"
)

