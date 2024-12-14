from django.shortcuts import render
from .models import Project
from rest_framework.decorators import api_view
from rest_framework.response import Response
from .serializers import UserSerializers
from rest_framework import status
from rest_framework.authtoken.models import Token
from django.contrib.auth.models import User
from django.shortcuts import get_object_or_404, redirect

@api_view(['POST'])
def login(request):
    user = get_object_or_404(User, username=request.data['username'])
    if not user.check_password(request.data['password']):
        return Response({"detail": "Not found"}, status=status.HTTP_404_NOT_FOUND)
    token, created = Token.objects.get_or_create(user=user)
    serializer = UserSerializers(isinstance=user)
    if user.role == 'user':
        return redirect('all_projects')
    else:
        return redirect('index')

@api_view(['POST'])
def signup(request):
    serializer = UserSerializers(data=request.data)
    if serializer.is_valid():
        serializer.save()
        user = User.objects.get(username=request.data['username'])
        user.set_password(request.data['password'])
        user.save()
        token = Token.objects.create(user=user)
        if request.data['role'] == 'user':
            return redirect('all_projects')
        else:
            return redirect('index')
        return Response({"token": token.key, "user": serializer.data})
    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


from rest_framework.decorators import authentication_classes, permission_classes
from rest_framework.authentication import SessionAuthentication, TokenAuthentication
from rest_framework.permissions import IsAuthenticated


@api_view(['GET'])
@authentication_classes([SessionAuthentication, TokenAuthentication])
@permission_classes([IsAuthenticated])
def test_token(request):
    return Response("passed for {}".format(request.user.email))

@api_view(['POST'])
@permission_classes([IsAuthenticated])
def logout(request):
       # Get the token associated with the user
   try:
       token = Token.objects.get(user=request.user)
       token.delete()  # Delete the token to log the user out
       return Response({"detail": "Successfully logged out."}, status=status.HTTP_200_OK)
   except Token.DoesNotExist:
       return Response({"detail": "Token not found."}, status=status.HTTP_400_BAD_REQUEST)

def index(request):
    return render(request, 'main/index.html')

def about(request):
    return render(request, 'main/about.html')

def all_projects(request):
    projects = Project.objects.all()
    return render(request, 'main/all_projects.html', {'title': 'Проекты на платформе', 'projects': projects})

def login_page(request):
       return render(request, 'authentication/login.html')

def signup_page(request):
    return render(request, 'authentication/signup.html')
