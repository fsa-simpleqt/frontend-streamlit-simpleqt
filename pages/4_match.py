import streamlit as st
from utils.match_utils import get_jd, get_cv, get_info_jd, get_info_cv, get_text_jd, get_text_cv, slice_id, match, prettify_match

st.set_page_config(page_title="CV Matcher")

st.header("CV Matcher", divider="rainbow")

jd_option = st.selectbox(
    "Select a Job Description from the Database",
    get_info_jd(get_jd()),
    index=None,
    placeholder="Select a Job Description"
)

if jd_option is not None:
    with st.expander("Preview"):
        id_jd = slice_id(jd_option)
        st.write(get_text_jd(get_jd(), id_jd))

cv_option = st.selectbox(
    "Select CV(s) from the Database",
    get_info_cv(get_cv()),
    index=None,
    placeholder="Select one or more CVs"
)

if cv_option is not None:
    id_cv = slice_id(cv_option)

if jd_option is not None and cv_option is not None:
    match_result = match(id_jd, id_cv)
    st.success("Matching Completed")

    col1, col2, col3 = st.columns(3)
    with col1:
        st.metric("Overall Match Percentage", f"{match_result.get('result').get('Overall Match Percentage:')}")
    with col2:
        st.metric("Skills Match Percentage:", f"{match_result.get('result').get('Skills Match').get('Match Percentage')}")
    with col3:
        st.metric("Experience Match Percentage:", f"{match_result.get('result').get('Experience Match').get('Match Percentage')}")

    st.subheader("Skills Match")
    st.write("• Required Skills")
    st.write(match_result.get("result").get("Skills Match").get("Required Skills"))
    st.write("• Candidate Skills") 
    st.write(match_result.get("result").get("Skills Match").get("Candidate Skills"))
    
    st.subheader("Experience Match")
    st.write("• Required Experience")
    st.write(match_result.get("result").get("Experience Match").get("Required Experience"))
    st.write("• Candidate Experience")
    st.write(match_result.get("result").get("Experience Match").get("Candidate Experience"))
    
    st.subheader("Explanation")
    st.write(match_result.get("result").get("Explanation"))
