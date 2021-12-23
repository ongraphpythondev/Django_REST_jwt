from django.http.response import HttpResponse
from django.shortcuts import redirect, render
from rest_framework import viewsets
from rest_framework.decorators import authentication_classes
from rest_framework.decorators import api_view , permission_classes
from rest_framework.permissions import IsAuthenticated
from django.contrib.auth.models import User 
from rest_framework_simplejwt.tokens import RefreshToken
from django.contrib.auth import authenticate
import requests



from rest_framework.response import Response

# Create your views here.
from rest_framework_simplejwt.serializers import TokenObtainPairSerializer
from rest_framework_simplejwt.views import TokenObtainPairView

class MyTokenObtainPairSerializer(TokenObtainPairSerializer):
    @classmethod
    def get_token(cls, user):
        token = super().get_token(user)

        data = dict()
        data['refresh'] = str(token)
        data['access'] = str(token.access_token)
        # self.request.session['sname'] = 'irfan'  
        # response.set_cookie('access', token.access_token)

        return token

class MyTokenObtainPairView(TokenObtainPairView):
    serializer_class = MyTokenObtainPairSerializer




@api_view(['GET'])
@permission_classes([IsAuthenticated])
def getNotes(request):
    user = request.user
    print(user.username)
    return Response("serializer.data")



# @api_view(['GET'])
def login(request):
    
    if request.method == "GET":
        return render(request ,"app/login.html")
    else:
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(username=username, password=password)
        if user:
            refresh = RefreshToken.for_user(user)
            # print(refresh)
            dict = {
                'refresh': str(refresh),
                'access': str(refresh.access_token),
            }
            # return requests.get("http://localhost:8000/profile/", headers={"Authorization": f"Bearer {refresh.access_token}"})
            response = redirect('/profile/')
            response.set_cookie("access-token" , refresh.access_token )
            response.set_cookie("refresh-token" , refresh )
            return response
        else:
            return render(request , "app/login.html" , {"dict":"user not found"})

@api_view(['GET'])
@permission_classes([IsAuthenticated])
def profile(request):
    
    if request.method == "GET":
        return render(request ,"app/profile.html")

def cookies(request):
    html = render(request , "app/login.html")
    html.set_cookie('TechVidvan', 'We are setting a cookie', max_age = None)
    html.set_cookie('ritesh', 'pandey', max_age = None)
    return html


def getcookies(request):
    show = request.COOKIES['ritesh']
    print(show)
    html = render(request , "app/profile.html")
    return html

