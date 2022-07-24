from django.shortcuts import render
from django.views import View

class FrontDashView(View):
    def dispatch(self, request, *args, **kwargs):
        self.template_name = "user_dashboard.html"
        self.args = {}
        return super().dispatch(request, *args, **kwargs)

    def get(self, request, *args, **kwargs):
        return render(request, self.template_name)