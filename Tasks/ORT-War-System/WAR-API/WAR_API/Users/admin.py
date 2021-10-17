from django.contrib import admin

# Register your models here.
from .models import Designation, Role, Users, ErrorLog, LevelMaster, UserToManager
# from tasks.models import Task,ExpressModeTask
from Department.models import Department
# from Codehelper.models import CodeHelper,Language
# from Project.models import Project

admin.site.register(Department)
admin.site.register( Designation)
admin.site.register(Role)
admin.site.register(Users)
admin.site.register( ErrorLog)
admin.site.register(LevelMaster)
admin.site.register( UserToManager)
# admin.site.register(Task)
# admin.site.register(Language)
# admin.site.register(CodeHelper)
# admin.site.register(ExpressModeTask)
# admin.site.register(Project)