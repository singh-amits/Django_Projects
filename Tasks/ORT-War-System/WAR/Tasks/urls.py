from django.contrib import admin
from django.urls import path, include
from . import views as v
urlpatterns = [
    path('admin/', admin.site.urls),
    path('addtask', v.addtask, name='addtask'),
    path('displaytask', v.displaytask, name='displaytask'),
    path('usertask', v.usertask, name='usertask')
]
