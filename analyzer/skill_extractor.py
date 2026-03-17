import pdfplumber
from .models import JobRoleSkill

def extract_text_from_pdf(pdf_path):
    text = ""
    
    with pdfplumber.open(pdf_path) as pdf:
        for page in pdf.pages:
            page_text = page.extract_text()
            if page_text:
                text += page_text
            
    return text.lower()

def extract_skills(text, job_role):
    detected_skills = []
    
    # Get required skills for the selected job role
    required_skills = JobRoleSkill.objects.filter(job_role=job_role).values_list("skill__name", flat=True)
    
    # Check if those skills exist in resume text
    for skill in required_skills:
        if skill.lower() in text:
            detected_skills.append(skill)
            
    return detected_skills 