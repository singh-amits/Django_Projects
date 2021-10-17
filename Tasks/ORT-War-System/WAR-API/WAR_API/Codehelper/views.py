from WAR_API import Codehelper
from django.shortcuts import render
from .models import Codehelper
from .serializers import GetCodehelperSerializer, PostCodehelperSerializer
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status
from rest_framework.status import (
    HTTP_400_BAD_REQUEST,
    HTTP_404_NOT_FOUND,
    HTTP_200_OK
)


@api_view(['GET'])
def (request, format=None):
    """
    List all tasks, or create a new task.
    """
    if request.method == 'GET':
        task = Codehelper.objects.all()
        serializer = GetCodehelperSerializer(task, many=True)
        return Response(serializer.data)
