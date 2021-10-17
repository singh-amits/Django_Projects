from django.shortcuts import render

from rest_framework.decorators import api_view
from rest_framework.views import APIView
from .serializers import DepartmentSerializer, DepartmentUpdateSerializer
from rest_framework.generics import ListAPIView
from Users.models import Designation, Role, Users, ErrorLog, LevelMaster, UserToManager
from .models import Department
from rest_framework.authentication import TokenAuthentication
from rest_framework.pagination import PageNumberPagination
from django.shortcuts import render
from django.contrib.auth import authenticate
from rest_framework.decorators import api_view, permission_classes
from rest_framework.permissions import AllowAny, IsAuthenticated
from rest_framework.response import Response
from rest_framework.status import (
    HTTP_400_BAD_REQUEST,
    HTTP_404_NOT_FOUND,
    HTTP_200_OK
)

# DISPLAY DEPARTMENT LIST-------------------------------------------------------------------------------------
# class departmentListAPI(ListAPIView):
#     serializer_class = DepartmentSerializer
#     queryset = Department.objects.all()
#     authentication_classes = (TokenAuthentication,)
#     permission_classes = (IsAuthenticated,)
#     pagination_class = PageNumberPagination

@api_view(['GET'])
def departmentListAPI(request, format=None):
    """
    List all tasks, or create a new task.
    """
    if request.method == 'GET':
        dept = Department.objects.all()
        serializer = DepartmentSerializer(dept, many=True)
        return Response(serializer.data)

# ADD DEPARTMENT-------------------------------------------------------------------------------------
@api_view(['POST'])
def addDepartment(request):
    user = request.user
    if user.is_superuser==True and user.is_admin ==True:
        try:
            serializer =DepartmentUpdateSerializer(data=request.data, context={'request':request})
        except Exception as e:
            print(e)
            return Response({'Error':'serializer not accepting data'})
        else:
            if serializer.is_valid():
                serializer.validated_data['CreatedBy'] = user
                print(serializer.initial_data)
                data ={}
                u = serializer.save()
                data['Status'] = 'Department added successfully'
                data['Department Name'] = u.DepartmentName
            else:
                data = serializer.errors
            return Response(data)
    else:
        return Response({'Error':'User has no permission to create'})

# DELETE DEPARTMENT-------------------------------------------------------------------------------------
@api_view(['GET'])
def departmentDelete(request):
    data = {"n":0,"Msg":"","Status":""} 
    try:
        departmentID = request.GET.get('departmentID')
        if departmentID is not None:
            department = Department.objects.filter(id = departmentID)
            if department is None:
                data['n']=0
                data['Msg']= 'DEPARTMENT DOES NOT EXIST'
                data['Status']="Failed"
            else:
                operation  = department.delete()
                if operation:
                    data['n']=1
                    data['Msg']= 'delete successfull'
                    data['Status']="Success"
                else:
                    data['n']=0
                    data['Msg']= 'delete failed'
                    data['Status']="Failed"
        else:
            data['n']=0
            data['Msg']= 'user.id is none'
            data['Status']="Failed"         
    except Exception as e:
        print(e)
        data['n']=0
        data['Msg']= 'try method failed'
        data['Status']="Failed"
    return Response(data =data)

# UPDATE DEPARTMENT-------------------------------------------------------------------------------------
@api_view(['POST'])
def departmentUpdate(request):
    data = {'n':'','Msg':'','Status':''}
    try:
        departmentID = request.query_params.get('departmentID')
        if departmentID is None:
            data['n']=0
            data['Msg']= 'department ID is none'
            data['Status']="Failed"
        else:
            try:
                department = Department.objects.get(id = departmentID)
            except Exception as e:
                print(e)
                data['n']=0
                data['Msg']= 'DEPARTMENT DOES NOT EXIST'
                data['Status']="Failed"
            else:
                serializer = DepartmentUpdateSerializer(department, request.data)
                if serializer.is_valid():
                    serializer.validated_data['UpdatedBy']  = request.user    
                    serializer.save()
                               
                    data['n']=1
                    data['Msg']= 'update successfull'
                    data['Status']="Success"
                else:
                    data = serializer.errors
                    # data['n']=0
                    # data['Msg']= 'update failed serializer invalid'
                    # data['Status']="Failed"
        return Response(data = data)

    except Exception as e:
        print(e)
        data['n']=0
        data['Msg']= 'try method failed'
        data['Status']="Failed"
        return Response(data = data)



