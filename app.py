import streamlit as st
from st_pages import Page, add_page_title, show_pages

def main():
    show_pages(
        [
            Page("app.py", "Home", "🏠"),
            Page("pages/1_jd_db.py", "Job Descriptions Database", "📄"),
            Page("pages/2_cv_db.py", "CVs Database", "📄"),
            Page("pages/3_test_db.py", "Exam Database", "📜"),
            Page("pages/4_match.py", "CV Matcher", "🤝"),
            Page("pages/5_retrieval.py", "Question Retrieval", "🔍"),
            Page("pages/6_generate_questions.py", "Generate Questions", "❓")
        ]
    )
    st.header("Home")

if __name__ == "__main__":
    main()
