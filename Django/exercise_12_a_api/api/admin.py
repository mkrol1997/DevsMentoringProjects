from django.contrib import admin
from .models import BugModel, UserModel, ProjectModel
# Register your models here.

admin.site.register(BugModel)
admin.site.register(UserModel)
admin.site.register(ProjectModel)
