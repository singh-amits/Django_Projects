from django.shortcuts import render,redirect, HttpResponse
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages
# from .forms import CreateUserForm
from django.contrib.auth.decorators import login_required
from django.conf import settings
# import requests

# @login_required(login_url='login')
def home(request): 
    return render(request, 'home.html')

# def loginPage(request):
#     # if request.user.is_authenticated:
#     #     return redirect('home')
#     # else:
#     if request.method == "POST":
#         username = request.POST.get('username')
#         password = request.POST.get('password')

#         user = authenticate(request, username=username, password=password)
#         if user is not None:
#             login(request, user)
#             return redirect('home')
#         else:
#             messages.info(request, "Username or Password is incorrect")
#     else:
#         context = {}
#         return render(request, 'accounts/login.html', context)

def loginPage(request):
    return render(request, 'accounts/login.html')
    
def addEmployee(request):
    return render(request, 'accounts/addEmployee.html')

# def addEmployee(request):
#     # if request.user.is_authenticated:
#     #     return redirect('home')
#     # else:
#     form = CreateUserForm()

#     if request.method == 'POST':
#         form = CreateUserForm(request.POST)
#         if form.is_valid():
#             form.save()
#             user = form.cleaned_data.get("Username")
#             p1 = form.cleaned_data.get("password1")
#             p2 = form.cleaned_data.get("password2")
#             if p1 == p2 :
#                 print(user)
#                 messages.success(
#                     request, "Account was created for " + user)
#                 return redirect('home')
#         else:
#             return render(request,'error.html', {'form':form})
#     else:
#         context = {'form': form}
#         return render(request, 'accounts/addEmployee.html', context)




from rest_framework.decorators import api_view
from rest_framework.views import APIView
from .serializers import UserSerializer, userRegisterSerializer, userUpdateSerializer
from rest_framework.generics import ListAPIView
from Users.models import Designation, Role, Users, ErrorLog, LevelMaster, UserToManager
from Department.models import Department
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

# USER LIST-------------------------------------------------------------------------------------
# class UserListAPI(ListAPIView):
#     serializer_class = UserSerializer
#     queryset = Users.objects.all()
#     authentication_classes = (TokenAuthentication,)
#     permission_classes = (IsAuthenticated,)
#     pagination_class = PageNumberPagination

@api_view(['GET'])
def UserListAPI(request, format=None):
    """
    List all tasks, or create a new task.
    """
    if request.method == 'GET':
        user = Users.objects.all()
        serializer = UserSerializer(user, many=True)
        return Response(serializer.data)



from rest_framework.authtoken.models import Token
from django.views.decorators.csrf import csrf_exempt

# LOGIN-------------------------------------------------------------------------------------
@csrf_exempt
@api_view(["POST"])
@permission_classes((AllowAny,))
def login(request):
    username = request.data.get("username")
    password = request.data.get("password")
    if username is None or password is None:
        return Response({'error': 'Please provide both username and password'},
                        status=HTTP_400_BAD_REQUEST)
    user = authenticate(username=username, password=password)
    if not user:
        return Response({'error': 'Invalid Credentials'},  
         
                        status=HTTP_404_NOT_FOUND)
    # token, _ = Token.objects.get_or_create(user=user)
    # token, _ = Token.objects.filter(user=user).update(key =)
    t,_ = Token.objects.get_or_create(user=user)
    t.delete()
    token, _ = Token.objects.get_or_create(user=user)
    return Response({'token': token.key},
                    status=HTTP_200_OK)

# LOGOUT USER-------------------------------------------------------------------------------------
#error - recursion depth exceeded--solve later
# def logout(request):
#     logout(request)
#     return Response({"success": _("Successfully logged out.")},
#                     status=status.HTTP_200_OK)



# ADD USER-------------------------------------------------------------------------------------
@api_view(['POST'])
def addUser(request):
    user = request.user
    if user.is_superuser==True and user.is_admin ==True:
        # userRegisterData = Users(CreatedBy=user)
        try:
            serializer = userRegisterSerializer(data=request.data, context={'request':request})
            
        except Exception as e:
            print(e)
            return Response({'Error':'serializer not accepting data'})
        else:
            if serializer.is_valid():
                print(serializer.initial_data)
                data ={}
                u = serializer.save()
                data['Status'] = 'Registered successfully'
                data['Email'] = u.email
                data['is_admin'] = u.is_admin
                data['is_staff'] = u.is_staff
                data['Username'] = u.Username
                data['Fullname'] = u.Fullname
            else:
                data = serializer.errors
            return Response(data)
    else:
        return Response({'Error':'User has no permission to create'})

# DELETE USER-------------------------------------------------------------------------------------
@api_view(['GET'])
def userDelete(request):
    data = {"n":0,"Msg":"","Status":""} 
    try:
        userID = request.GET.get('userID')
        # userID = request.query_params.get('userID')
        if userID is not None:
            user = Users.objects.filter(id = userID)
            if user is None:
                data['n']=0
                data['Msg']= 'USER DOES NOT EXIST'
                data['Status']="Failed"
            else:
                operation  = user.delete()
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

#chk how data is coming from front end for foreign keys...accordingly use userserializer or userRegisterSerializer
# UPDATE USER-------------------------------------------------------------------------------------
@api_view(['POST'])
def userUpdate(request):
    data = {'n':'','Msg':'','Status':''}
    try:
        userID = request.query_params.get('userID')
        if userID is None:
            data['n']=0
            data['Msg']= 'User ID is none'
            data['Status']="Failed"
        else:
            try:
                user = Users.objects.get(id = userID)
            except Exception as e:
                print(e)
                data['n']=0
                data['Msg']= 'USER DOES NOT EXIST'
                data['Status']="Failed"
            else:
                serializer = userUpdateSerializer(user, request.data)
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


