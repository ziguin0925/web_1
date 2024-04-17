from django import forms
from django.contrib.auth.forms import UserCreationForm
from .models import User


class UserForm(UserCreationForm):
    email = forms.EmailField(label="이메일")
    last_name = forms.CharField(label = "last_name")
    first_name = forms.CharField(label="first_name")
    adress1 = forms.CharField(label="adress1")
    adress2 = forms.CharField(label="adress2")
    phone_number = forms.CharField(label="phone_number")
    birth_id1 = forms.CharField(label="birth_id1")
    birth_id2 = forms.CharField(label="birth_id2")

    class Meta:
        model = User # 사용할 모델정보
        fields = ("last_name","first_name","username","adress2","adress1","email","phone_number","birth_id1","birth_id2", "password") # 사용할 속성 정보


