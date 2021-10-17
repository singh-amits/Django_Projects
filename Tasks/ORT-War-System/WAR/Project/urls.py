from django.contrib import admin
from django.urls import path, include
from . import views as v
urlpatterns = [
    path('admin/', admin.site.urls),
    path('project', v.project, name='project'),
    path('displaydept', v.displaydept, name='displaydept'),
    path('displayba', v.displayba, name='displayba')

]
