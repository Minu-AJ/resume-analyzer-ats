from django.contrib import admin
from .models import Skill, JobRole, JobRoleSkill, Resume

admin.site.register(Skill)
admin.site.register(JobRole)
admin.site.register(JobRoleSkill)

class ResumeAdmin(admin.ModelAdmin):
    list_display = ('name', 'job_role', 'match_score')
    
admin.site.register(Resume, ResumeAdmin)
