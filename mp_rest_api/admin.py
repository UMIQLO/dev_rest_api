from django.contrib import admin
from .models import *
# Register your models here.
models = [Music,UserGroup,PlayListType,UserPlayList]
admin.site.register(models)