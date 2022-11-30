from django.shortcuts import render
from django.http import HttpResponse, JsonResponse
from django.views.decorators.csrf import csrf_exempt
from rest_framework.parsers import JSONParser
from .models import CustomUser
from .serializers import CustomUserSerializer

@csrf_exempt
def CustomUser_list(request):
    """
    List all code snippets, or create a new snippet.
    """
    if request.method == 'GET':
        user = CustomUser.objects.all()
        serializer = CustomUserSerializer(user, many=True)
        return JsonResponse(serializer.data, safe=False)

    elif request.method == 'POST':
        data = JSONParser().parse(request)
        serializer = CustomUserSerializer(data=data)
        if serializer.is_valid():
            serializer.save()
            return JsonResponse(serializer.data, status=201)
        return JsonResponse(serializer.errors, status=400)
