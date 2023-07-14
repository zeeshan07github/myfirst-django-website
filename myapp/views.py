from django.shortcuts import render

# Create your views here.
def home(request):
    return render(request,'home.html')
def index(request):
    return render(request,'index.html')
def base(request):
    return render(request,'base.html')
def footer(request):
    return render(request,'footer.html')
def header(request):
    return render(request,'header.html')