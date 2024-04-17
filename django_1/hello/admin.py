from django.contrib import admin

from .models import  Post, Mention


admin.site.register(Post)
admin.site.register(Mention)