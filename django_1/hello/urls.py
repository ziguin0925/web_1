from django.urls import path
from hello import views
from common import views as common_views
from django.contrib.auth import views as auth_views

urlpatterns =[
    path("", views.home, name="home"),
    path("login/" , auth_views.LoginView.as_view(template_name='login.html'), name="login"),
    path('logout/', views.loged_out,name='logout'),
    path("about/" , views.about, name="about"),
    path("contact/" , views.contact, name="contact"),
    path("infra/", views.infra , name="infra"),
    path("repaircar/", views.repaircar , name="repaircar"),
    path("mention/", views.mention , name="mention"),
    path('community/<int:pk>/',views.post_read, name="post_read"),
    path("community/", views.community, name="community"),
    path("postwrite/", views.postwrite, name="postwrite"),
    path("buycar/", views.buycar, name="buycar"),
    path("signup/", common_views.signup , name="signup"),
    path("insurance/", views.insurance , name="insurance"),
    path("oldcar/", views.oldcar , name="oldcar"),
    path("test/", views.test , name="test"),


    

    
]
