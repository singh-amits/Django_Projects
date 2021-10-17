from django.shortcuts import render,redirect,HttpResponseRedirect
from .forms import Task_assign
from .models import task
from datetime import datetime,date
from django.contrib import messages as msg

# Create your views here.
def Tododetail(req):

    if req.method == 'POST':
        dd = req.POST.get("deadline")
        print(dd , "#"*60 , date.today())
        if dd[:10] < str(date.today()) and dd[11:] < str(datetime.now().strftime("%H:%M")):
            msg.add_message(req,msg.SUCCESS,'Deadline is not valid')
            print("hello" *20)

        else:
            assign = task(Task_title = req.POST.get("Task_title"),
                            Task_img = req.POST.get("Task_img"),
                            description_img = req.POST.get("description_img"),
                            description = req.POST.get("description"),
                            deadline = dd,
                            date_joined = datetime.now())
            assign.save()
        taskAssigned = Task_assign()

    else:
        taskAssigned = Task_assign()
    tsk = task.objects.all()
    return render(req, "todo/index.html",{'form': taskAssigned, 'task': tsk})

def update(req,id):

    if req.method == 'POST':
        ti = task.objects.get(pk = id)
        tsk = task(req.POST , instance = tsk)
        tsk.save()
        # assign = task(Task_title = req.POST.get("Task_title"),
        #                 Task_img = req.POST.get("Task_img"),
        #                 discription_img = req.POST.get("discription_img"),
        #                 discription = req.POST.get("discription"),
        #                  deadline = req.POST.get("deadline"))
        # assign.save()
        # taskAssigned = Task_assign()

    else:
        ti = task.objects.get(pk = id)
        tsk = Task_assign(instance = ti)
    return render(req, "todo/update.html",{'task':tsk})



def delete_data(req,id):
    if req.method == 'POST':
        ti = task.objects.get(pk = id)

        ti.delete()
        return HttpResponseRedirect ("/")