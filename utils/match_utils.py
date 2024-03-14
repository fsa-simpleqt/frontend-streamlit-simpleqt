import requests
import json
import re

def get_cv():
    # Define the URL
    url = "https://millmin-fsa-project-cv.hf.space/modules/crud_cvs_router/"
    # Send a GET request
    response = requests.get(url)
    # Print the response content
    return json.loads(response.content.decode("utf-8"))

# def get_jd():
#     # Define the URL
#     url = "https://millmin-fsa-project-cv.hf.space/modules/crud_jds_router/"
#     # Send a GET request
#     response = requests.get(url)
#     # Print the response content
#     return json.loads(response.content.decode("utf-8"))

def get_jd():
    # Define the URL
    url = "https://millmin-fsa-project-cv.hf.space/modules/crud_jds_router/"
    # Send a GET request
    response = requests.get(url)
    print(response.content)  # Add this line
    # Print the response content
    return json.loads(response.content.decode("utf-8"))


def get_info_jd(jd_list):
    info_jd_list = [f"{jd.get("position_applied_for")} [{jd.get("id_jd")}]" for jd in jd_list]
    return info_jd_list

def get_info_cv(cv_list):
    info_cv_list = [f"{cv.get("name_candidate")} - {cv.get("apply_position")} [{cv.get("id_cv")}]" for cv in cv_list]
    return info_cv_list

def match(id_jd, id_cv):
    id_jd_0 = re.search(r'\[(.*?)\]', id_jd).group(1)
    id_cv_0 = re.search(r'\[(.*?)\]', id_cv).group(1)

    url = "https://millmin-fsa-project-cv.hf.space/modules/cvmatching/matching/"
    completed_url = f"{url.rstrip("/")}?id_jd={id_jd_0}&id_cv={id_cv_0}"
    response = requests.post(completed_url)
    return json.loads(response.content.decode("utf-8"))

def prettify_match(match):
    overall_match = match.get("Overall Match Percentage:")
    skills_match = match.get("Skills Match").get("Match Percentage")
    experience_match = match.get("Experience Match").get("Match Percentage")
    required_skills = match.get("Skills Match").get("Required Skills")
    candidate_skills = match.get("Skills Match").get("Camdidate  Skills")
    required_experience = match.get("Experience Match").get("Required Experience")
    candidate_experience = match.get("Experience Match").get("Candidate Experience")
    return overall_match, skills_match, experience_match, required_skills, candidate_skills, required_experience, candidate_experience