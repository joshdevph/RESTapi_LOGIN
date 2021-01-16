from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.response import Response
from django.http import JsonResponse
from django.contrib.auth import login, logout
from .serializers import LoginSerializer
from rest_framework.authtoken.serializers import AuthTokenSerializer
from rest_framework import status
from django.core.exceptions import ValidationError

class LoginApiView(APIView):
    def post(self, request):
        serializer = AuthTokenSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        user = serializer.validated_data['user']
        login(request, user)
        user_id = user.id
        is_staff = user.is_staff
        if user.is_authenticated:
            logged_in = True
            request.session['logged_in'] = logged_in
            fname = user.first_name
            lname = user.last_name
            request.session['user_id'] = user_id
            request.session['is_staff'] = is_staff
            request.session['fullname'] = fname + ' ' + lname

            if is_staff == False:
                data = {
                    "status" : logged_in
                }
            else:
                logged_in = False
                data = {
                    "status" : logged_in
                }

        return JsonResponse(data)
            

class LogoutAPI(APIView):
    def post(self, request):
        print('Logged Out')
        logout(request)
        data = {
            "text":"Logged out"
        }
        return Response(data)
