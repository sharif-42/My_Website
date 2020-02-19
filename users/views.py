from django.contrib.auth import authenticate, login, logout
from django.shortcuts import redirect
from rest_framework import status
from rest_framework.renderers import TemplateHTMLRenderer
from rest_framework.response import Response
from rest_framework.views import APIView

from users.forms import LoginForm, SignUpForm, ChangePasswordForm
from users.serializers import LoginSerializer


class Home(APIView):
    renderer_classes = [TemplateHTMLRenderer]
    template_name = 'index.html'

    def get(self, request):
        return Response({}, status=status.HTTP_200_OK)


class SignUp(APIView):
    renderer_classes = [TemplateHTMLRenderer]
    template_name = 'signup.html'

    def get(self, request):
        form = SignUpForm()
        queryset = "This is Home Page"
        return Response({'form': form})

    def post(self, request):
        form = SignUpForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('/home/')
            # return Response({'form': form}, status=status.HTTP_200_OK)
        return Response({'form': form}, status=status.HTTP_200_OK)


class Login(APIView):
    renderer_classes = [TemplateHTMLRenderer]
    template_name = 'login.html'

    def get(self, request):
        form = LoginForm()
        return Response({'form': form})

    def post(self, request):
        form = LoginForm()
        serializer = LoginSerializer(data=request.data)
        if serializer.is_valid():
            print(serializer.data)
            user = authenticate(request, username=serializer.data['username'], password=serializer.data['password'])
            if user is not None:
                print("USERRRRRRRRRRRRRRR")
                login(request, user)
            print(request.data)
            return redirect('/home/')
        return Response({'form': form}, status=status.HTTP_200_OK)


class Logout(APIView):
    def get(self, request):
        logout(request)
        return redirect('/home')

class ChangePassword(APIView):
    renderer_classes = [TemplateHTMLRenderer]
    template_name = 'password_change.html'

    def get(self, request):
        form = ChangePasswordForm()
        return Response({'form': form})

    def post(self, request):
        form = ChangePasswordForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('/home/')
        return Response({'form': form}, status=status.HTTP_200_OK)