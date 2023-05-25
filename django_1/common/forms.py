from django import forms
from django.contrib.auth.forms import UserCreationForm
from .models import User


class UserForm(UserCreationForm):
    
    
    class Meta:
        model = User # 사용할 모델정보
        fields = ("last_name","first_name","username","adress2","adress1","email","phone_number","birth_id2","birth_id1","username", "password") # 사용할 속성 정보


