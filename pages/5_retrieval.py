import streamlit as st
from utils.retrieval import get_info_jd, get_jd, get_text_jd, slice_id, retrieve_test

# Set up the title and introduction of the web app
st.header('Question Retrieval', divider="rainbow")

# Fetch JDs when the app loads
jds = get_jd()

if jds:
    # Displaying the fetched JDs
    jd_options = get_info_jd(jds)
    jd_selected = st.selectbox('Select a JD:', jd_options)

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
else:
    st.error('Failed to fetch JDs')

st.write(retrieve_test(id_jd))

# if id_jd is not None:
#     # Button to retrieve test
#     if st.button('Retrieve Test'):
#         test = retrieve_test(id_jd)
#         if test:
#             # Displaying the fetched test
#             st.write(f"Test: {test}")
#         else:
#             st.error('Failed to retrieve test')


