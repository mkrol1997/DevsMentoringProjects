from django.contrib import admin
from .models import UserModel, BugModel, ProjectModel
# Register your models here.

admin.site.register(BugModel)
admin.site.register(ProjectModel)
admin.site.register(UserModel)
