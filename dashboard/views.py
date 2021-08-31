from django.shortcuts import render

# Create your views here.
def dashboardView(request):
    template_name = 'dashboard/dashboard_home.html'

    return render(request,template_name)