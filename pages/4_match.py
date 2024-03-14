import streamlit as st
from utils.match_utils import get_jd, get_cv, get_info_jd, get_info_cv, match, prettify_match

st.set_page_config(page_title="CV Matcher")

jd_option = st.selectbox(
    "Select a Job Description in the Database",
    get_info_jd(get_jd()),
    index=None,
    placeholder="Select a Job Description"
)

cv_option = st.selectbox(
    "Select CV(s) in the Database",
    get_info_cv(get_cv()),
    index=None,
    placeholder="Select one or more CVs"
)

if jd_option is not None and cv_option is not None:
    st.text((match(jd_option, cv_option)))
else:
    st.info("Result")

# overall_match, skills_match, experience_match, required_skills, candidate_skills, required_experience, candidate_experience = prettify_match(match(jd_option, cv_option))
