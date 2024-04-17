
import re

from django.utils import timezone

from django.shortcuts import render, redirect

from django.contrib.auth import *

from .models import Post, Mention, Recom

from django.contrib.auth import authenticate
from common.models import User
from .car import *
from django.contrib.auth.decorators import login_required



#클래스형 view(Class Based View)

def home(request): # 함수형 view(FBV)
            if (request.user.is_authenticated):
                user=request.user
                user_id=User.objects.get(username=user)
                try:
                    user_price=Mention.objects.get(User_id=user_id.id)
                except:
                    return render(request, "hello/home.html")
                good=Recom.objects.get(num=user_price.price)
                return render(request, "hello/home.html",{'good':good})

            else:
                return render(request, "hello/home.html")

def about(request):
    return render(request, "hello/about.html")

def contact(request):
    return render(request, "hello/contact.html")

def infra(request):
    return render(request,'hello/infra.html')

def repaircar(request):
    return render(request,'hello/repaircar.html')



def buycar(request):
    return render(request,'hello/buycar.html')
    
def insurance(request):
    return render(request,'hello/insurance.html')

def oldcar(request):
    return render(request,'hello/oldcar.html')

def test(request):
    return render(request,'hello/test.html')



def postwrite(request):
    if request.method == 'POST':
        new_article=Post.objects.create(
            postname=request.POST["postname"],
            text=request.POST["text"],
            create_date=timezone.now()
        )
        return redirect('/community/')
    return render(request, 'hello/postwrite.html')

def community(request):
    post_list = Post.objects.all()
    return render(request,'hello/community.html',{'post_list':post_list})

def post_read(request,pk):
    # 게시글(Post) 중 pk(primary_key)를 이용해 하나의 게시글(post)를 검색
    post = Post.objects.get(pk=pk)
    # posting.html 페이지를 열 때, 찾아낸 게시글(post)을 post라는 이름으로 가져옴
    return render(request, 'hello/post_read.html', {'post':post})

@login_required
def mention(request):
    if request.method == 'POST':
        u_id=int(request.POST["User_id"])
        try:
            key=Mention.objects.get(User_id=u_id)

            if (key):
                cancel=Mention.objects.get(User_id=u_id)
                cancel.delete()
                car_recom=Mention.objects.create(
                price=request.POST["price"],
                frequency=request.POST["frequency"],
                distance=request.POST["distance"],
                location=request.POST["location"],
                importance=request.POST["importance"],
                User_id=User.objects.get(pk=u_id),
            )
            
        
        except:
            car_recom=Mention.objects.create(
            price=request.POST["price"],
            frequency=request.POST["frequency"],
            distance=request.POST["distance"],
            location=request.POST["location"],
            importance=request.POST["importance"],
            User_id=User.objects.get(pk=u_id),
        )
        score(request.POST["price"])
        good=Recom.objects.get(num=request.POST["price"])
        return redirect('/', {'good':good})
    return render(request, 'hello/mention.html')



def loged_out(request):
    logout(request)
    return render(request, 'hello/home.html')
