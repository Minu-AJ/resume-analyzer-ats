from django.shortcuts import render,redirect
from .forms import ResumeUploadForm
from .skill_extractor import extract_skills, extract_text_from_pdf
from .models import JobRoleSkill, Resume


# Upload Resume view
def upload_resume(request):
    
    if request.method == 'POST':
        
        form = ResumeUploadForm(request.POST,request.FILES)
        
        if form.is_valid():
           resume = form.save()
           
           # Get file path
           pdf_path = resume.resume_file.path
           
           # Extract text from resume
           text = extract_text_from_pdf(pdf_path)
           
           # Detect skill
           detected_skills = extract_skills(text, resume.job_role)
           
           # Get required skills from db
           required_skills = JobRoleSkill.objects.filter(job_role=resume.job_role).values_list("skill__name", flat=True)
           required_skills = list(required_skills)
           
           # Calculate match score
           if len(required_skills) > 0:
               match_score = (len(detected_skills)/len(required_skills)) * 100
           else:
               match_score = 0
        
        # Save score       
        resume.match_score = match_score
        resume.save()
        
        # Debug output(optional)       
        print("Required Skills:", required_skills)
        print("Detected Skills:", detected_skills)
        print("Match score:", match_score)
           
    else:
        form = ResumeUploadForm()
    return render(request, 'upload_resume.html', {'form':form})


# Resume List View(Ranking page)
def resume_list(request):
    resumes = Resume.objects.all().order_by('-match_score')
    
    return render(request, 'resume_list.html', {'resumes':resumes})
            