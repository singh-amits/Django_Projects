from django.shortcuts import render
from .models import TaskMaster
from .serializers import GetTaskMasterSerializer, PostTaskMasterSerializer
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status
from rest_framework.status import (
    HTTP_400_BAD_REQUEST,
    HTTP_404_NOT_FOUND,
    HTTP_200_OK
)


@api_view(['GET'])
def taskList(request, format=None):
    """
    List all tasks, or create a new task.
    """
    if request.method == 'GET':
        task = TaskMaster.objects.all()
        serializer = GetTaskMasterSerializer(task, many=True)
        return Response(serializer.data)


@api_view(['POST'])
def addNewTask(request, format=None):
    if request.method == 'POST':
        serializer = PostTaskMasterSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


@api_view(['GET'])
def deleteTask(request):
    data = {"n": 0, "Msg": "", "Status": ""}
    try:
        taskID = request.GET.get('taskID')
        if taskID is not None:
            task = TaskMaster.objects.filter(id=taskID)
            if task is None:
                data['n'] = 0
                data['Msg'] = 'TASK DOES NOT EXIST'
                data['Status'] = "Failed"
            else:
                operation = task.delete()
                if operation:
                    data['n'] = 1
                    data['Msg'] = 'delete successfull'
                    data['Status'] = "Success"
                else:
                    data['n'] = 0
                    data['Msg'] = 'delete failed'
                    data['Status'] = "Failed"
        else:
            data['n'] = 0
            data['Msg'] = 'task.id is none'
            data['Status'] = "Failed"
    except Exception as e:
        print(e)
        data['n'] = 0
        data['Msg'] = 'try method failed'
        data['Status'] = "Failed"
    return Response(data=data)


@api_view(['POST'])
def updateTask(request):
    data = {'n': '', 'Msg': '', 'Status': ''}
    try:
        taskID = request.query_params.get('taskID')
        task = TaskMaster.objects.get(id=taskID)
        if taskID is None:
            data['n'] = 0
            data['Msg'] = 'task ID is none'
            data['Status'] = "Failed"
        else:
            try:
                task = TaskMaster.objects.get(id=taskID)
            except Exception as e:
                print(e)
                data['n'] = 0
                data['Msg'] = 'TASK DOES NOT EXIST'
                data['Status'] = "Failed"
            else:
                serializer = PostTaskMasterSerializer(task, request.data)
                if serializer.is_valid():
                    # serializer.validated_data['UpdatedBy']  = request.task
                    serializer.save()

                    data['n'] = 1
                    data['Msg'] = 'update successfull'
                    data['Status'] = "Success"
                else:
                    data = serializer.errors
        return Response(data=data)

    except Exception as e:
        print(e)
        data['n'] = 0
        data['Msg'] = 'try method failed'
        data['Status'] = "Failed"
        return Response(data=data)
