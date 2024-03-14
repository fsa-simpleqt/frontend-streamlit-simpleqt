import requests
import json
import re
import os
from dotenv import load_dotenv

load_dotenv()
os.environ['BACKEND_URL_API'] = os.getenv('BACKEND_URL_API')
BACKEND_URL_API = os.environ.get("BACKEND_URL_API")

def get_jd():
    # Define the URL
    url = f"{BACKEND_URL_API}/modules/crud_jds_router/"
    # Send a GET request
    response = requests.get(url)
    # Print the response content
    return json.loads(response.content.decode("utf-8"))

def get_cv():
    # Define the URL
    url = f"{BACKEND_URL_API}/modules/crud_cvs_router/"
    # Send a GET request
    response = requests.get(url)
    # Print the response content
    return json.loads(response.content.decode("utf-8"))

def get_info_jd(jd_list):
    info_jd_list = [f"{jd.get("position_applied_for")} [{jd.get("id_jd")}]" for jd in jd_list]
    return info_jd_list

def get_info_cv(cv_list):
    info_cv_list = [f"{cv.get("name_candidate")} - {cv.get("apply_position")} [{cv.get("id_cv")}]" for cv in cv_list]
    return info_cv_list

def get_text_jd(jd_list, id_jd):
    for jd in jd_list:
        if jd.get("id_jd") == id_jd:
            return jd.get("jd_text")
    return None

def get_text_cv(cv_list, id_cv):
    for jd in cv_list:
        if jd.get("id_cv") == id_cv:
            return jd.get("cv_content")
    return None

def slice_id(info: str):
    return re.search(r'\[(.*?)\]', info).group(1)

def match(id_jd, id_cv):
    url = f"{BACKEND_URL_API}/modules/cvmatching/matching/"
    completed_url = f"{url.rstrip("/")}?id_jd={id_jd}&id_cv={id_cv}"
    response = requests.post(completed_url)
    return json.loads(response.content.decode("utf-8"))

def prettify_match(match):
    overall_match = match.get("Overall Match Percentage:")
    skills_match = match.get("Skills Match").get("Match Percentage")
    experience_match = match.get("Experience Match").get("Match Percentage")
    required_skills = match.get("Skills Match").get("Required Skills")
    candidate_skills = match.get("Skills Match").get("Candidate  Skills")
    required_experience = match.get("Experience Match").get("Required Experience")
    candidate_experience = match.get("Experience Match").get("Candidate Experience")
    explanation = match.get("Explanation")
    return overall_match, skills_match, experience_match, required_skills, candidate_skills, required_experience, candidate_experience, explanation