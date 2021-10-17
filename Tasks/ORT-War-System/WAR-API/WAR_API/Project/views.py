from django.shortcuts import render
from .models import Project
from .serializers import GetProjectSerializer, PostProjectSerializer
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status
from rest_framework.status import (
    HTTP_400_BAD_REQUEST,
    HTTP_404_NOT_FOUND,
    HTTP_200_OK
)


@api_view(['GET'])
def projectList(request, format=None):
    """
    List all projects, or create a new project.
    """
    if request.method == 'GET':
        task = Project.objects.all()
        serializer = GetProjectSerializer(Project, many=True)
        return Response(serializer.data)


@api_view(['POST'])
def addNewProject(request, format=None):
    if request.method == 'POST':
        serializer = PostProjectSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


@api_view(['GET'])
def deleteProject(request):
    data = {"n": 0, "Msg": "", "Status": ""}
    try:
        projectID = request.GET.get('projectID')
        if projectID is not None:
            project = Project.objects.filter(id=projectID)
            if project is None:
                data['n'] = 0
                data['Msg'] = 'Project DOES NOT EXIST'
                data['Status'] = "Failed"
            else:
                operation = Project.delete()
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
            data['Msg'] = 'project.id is none'
            data['Status'] = "Failed"
    except Exception as e:
        print(e)
        data['n'] = 0
        data['Msg'] = 'try method failed'
        data['Status'] = "Failed"
    return Response(data=data)


@api_view(['POST'])
def updateProject(request):
    data = {'n': '', 'Msg': '', 'Status': ''}
    try:
        projectID = request.query_params.get('projectID')
        project = Project.objects.get(id=projectID)
        if projectID is None:
            data['n'] = 0
            data['Msg'] = 'project ID is none'
            data['Status'] = "Failed"
        else:
            try:
                project = Project.objects.get(id=projectID)
            except Exception as e:
                print(e)
                data['n'] = 0
                data['Msg'] = 'Project DOES NOT EXIST'
                data['Status'] = "Failed"
            else:
                serializer = PostProjectSerializer(project, request.data)
                if serializer.is_valid():
                    # serializer.validated_data['UpdatedBy']  = request.project
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
