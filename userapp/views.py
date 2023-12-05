from django.shortcuts import render, HttpResponse


# Create your views here.
def sayHello(request):
    return HttpResponse("Django Project is created & web page is executed")

def html_page(request):
    return render(request,'index.html')


