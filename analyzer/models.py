from django.db import models

class Skill(models.Model):
    name = models.CharField(max_length=100)
    
    def __str__(self):
        return self.name
    
class JobRole(models.Model):
    title = models.CharField(max_length=100)
    
    def __str__(self):
        return self.title
    
class JobRoleSkill(models.Model):
    job_role = models.ForeignKey(JobRole, on_delete=models.CASCADE)
    skill = models.ForeignKey(Skill, on_delete=models.CASCADE)
    
    class Meta:
        unique_together = ('job_role', 'skill')
    
    def __str__(self):
        return f"{self.job_role.title}-{self.skill.name}"
    
class Resume(models.Model):
    name = models.CharField(max_length=100)
    job_role = models.ForeignKey(JobRole, on_delete=models.CASCADE)
    resume_file = models.FileField(upload_to='resumes/')
    uploaded_at = models.DateTimeField(auto_now_add=True)
    match_score = models.FloatField(null=True, blank=True)
    
    def __str__(self):
        return self.name


    
        
        
