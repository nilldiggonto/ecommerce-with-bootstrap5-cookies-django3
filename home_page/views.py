from django.shortcuts import render

# Create your views here.
def homeView(request):
    template_name = 'home/home.html'
    return render(request,template_name)

def category(request):
    template_name = 'home/category.html'
    return render(request,template_name)