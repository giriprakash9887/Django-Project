from django.http import HttpResponse
from django.shortcuts import redirect
from django.urls import reverse
from django.views import View

# def home(request):
#     return HttpResponse("welcome to Home Page")


# def contact(request):
#     return HttpResponse("Contact view based function")

# class About(View):
#     def get(self,request):
#         return HttpResponse("Class based view")


def profile(request,username):
    return HttpResponse(f"Hi {username}")

# def product_detail(request,id):
#     return HttpResponse(f"Product ID: {id}")

def product_detail(request,id):
    return redirect('blog-post', id)


def blog_post(request,slug):
    return HttpResponse(f"Blog-Post: {slug}")

def item_detail(request,item_id):
    return HttpResponse(f"Item UUID : {item_id}")

def media_handler(request,path_file):
    return HttpResponse(f"Path file is: {path_file}")


# def go_to_post(request):
#     url = reverse('blog-post', args=['What-is-django'])
#     return HttpResponse(f"URL Path: {url}")


def go_to_post(request):
    url = reverse('go-to-post')
    return HttpResponse(f"URL Path: {url}")