from django.views.generic import TemplateView
from django.views import View
from django.shortcuts import render

class HomeView(TemplateView):
    template_name = 'core/index.html'


class CricketView(View):
    def get(self, request):
        return render(request, 'core/cricket.html')
    

class LoginView(View):
    def get(self, request):
        return render(request, 'core/login.html')


class CreateAccountView(View):
    def get(self, request):
        return render(request, 'core/create-acount.html')