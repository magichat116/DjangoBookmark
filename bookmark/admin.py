from django.contrib import admin

from .models import Bookmark

# Register your models here.
admin.site.register(Bookmark) #관리자 페이지에 미리 모델을 등록