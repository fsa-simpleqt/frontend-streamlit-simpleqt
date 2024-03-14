
# import streamlit as st
# from utils.retrieval import get_info_jd, get_jd, get_text_jd, slice_id

# # Set up the title and introduction of the web app
# st.title('JD Selection and Analysis Tool')
# st.write('Use this tool to fetch and analyze job descriptions (JD).')

# # Button to fetch JDs
# if st.button('Fetch JDs'):
#     jds = get_jd()
#     if jds:
#         # Displaying the fetched JDs
#         jd_options = get_info_jd(jds)
#         jd_selected = st.selectbox('Select a JD:', jd_options)
        
#         # Extract the ID from the selected option
#         id_jd = slice_id(jd_selected)
        
#         # Get the text of the selected JD
#         jd_text = get_text_jd(jds, id_jd)
        
#         # Display the selected JD ID, position, and text
#         st.write(f"You selected: {jd_selected} with ID {id_jd}")
#         st.write(f"JD Text: {jd_text}")
        
#     else:
#         st.error('Failed to fetch JDs')


import streamlit as st
from utils.retrieval import get_info_jd, get_jd, get_text_jd, slice_id

# Set up the title and introduction of the web app
st.title('JD Selection and Analysis Tool')
st.write('Use this tool to fetch and analyze job descriptions (JD).')

# Fetch JDs when the app loads
jds = get_jd()
if jds:
    # Displaying the fetched JDs
    jd_options = get_info_jd(jds)
    jd_selected = st.selectbox('Select a JD:', jd_options)

    # Button to display selected JD
    if st.button('Display Selected JD') :
        # Extract the ID from the selected option
        id_jd = slice_id(jd_selected)

        # Get the text of the selected JD
        jd_text = get_text_jd(jds, id_jd)

        # Display the selected JD ID, position, and text
        st.info(f"You selected: {jd_selected} with ID {id_jd}")
        with st.expander('Preview'):
            st.write(f"JD Text: {jd_text}")
else:
    st.error('Failed to fetch JDs')
