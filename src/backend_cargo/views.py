
from cProfile import Profile
from django.shortcuts import redirect, render
from django.views import View   

from django.contrib.auth.mixins import LoginRequiredMixin

from django.contrib import messages

from .forms import UserLoginForm

from .models import Profile

class DashboardView(LoginRequiredMixin, View):
    def get(self, request):
        profile_qs = Profile.objects.get(user=request.user)  
        self.args={
            "profile_qs":profile_qs
        }
        return render(request, 'dashboard.html',self.args)
