from django import forms
from .models import Resume


class ResumeUploadForm(forms.ModelForm):
    
    class Meta:
        model = Resume
        fields = ['name', 'job_role', 'resume_file']
        
        