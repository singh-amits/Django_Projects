from django.contrib import admin
from enroll.models import Student


@admin.register(Student)
class StudentAdmin(admin.ModelAdmin):
    list_display=('id', 'stuid', 'stuname', 'stuemail', 'stupass')

# Register your models here.
#admin.site.register(Student, StudentAdmin)
