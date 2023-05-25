
import re

from django.utils import timezone

from django.shortcuts import render, redirect

from django.contrib.auth import authenticate, login

from .models import Post





def home(request):
    return render(request, "hello/home.html")

def about(request):
    return render(request, "hello/about.html")

def contact(request):
    return render(request, "hello/contact.html")

def infra(request):
    return render(request,'hello/infra.html')

def repaircar(request):
    return render(request,'hello/repaircar.html')

def mention(request):
    return render(request,'hello/mention.html')

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
