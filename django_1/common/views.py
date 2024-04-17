
from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login 
from django.contrib.auth.hashers import make_password
from .forms import UserForm
from .models import User

#from django.contrib.auth.models import User




# Create your views here.


def signup(request):
    if request.method == "POST":
        form = UserForm(request.POST)

        if form.is_valid():
            form.save()
            username = form.cleaned_data.get('username')
            raw_password = form.cleaned_data.get('password1')
            user = authenticate(username=username, password = raw_password)
            login(request, user)
            return redirect('index')

        '''
        username=request.POST["username"]
        first_name=request.POST["first_name"]
        last_name=request.POST["last_name"]
        email=request.POST["email"]
        birth_id11=request.POST["birth_id1"]
        birth_id22=request.POST["birth_id2"]
        pass_word=request.POST["password1"]
        adress1=request.POST.get('adress1','')
        adress2=request.POST.get('adress2','')
        phone_number=request.POST.get('phone_number','')
        password=make_password(pass_word)
        user=User.objects.create(birth_id1=birth_id11,
                            birth_id2=birth_id22,
                            username=username,
                            first_name=first_name,
                            last_name=last_name,
                            email=email,
                            password=password,
                            adress1=adress1,
                            adress2=adress2,
                            phone_number=phone_number)

        return redirect('/login/')
    '''
    else:
        form = UserForm()
    return render(request, 'signup.html', {'form':form})

