from django.db import models
from django.urls import reverse

# Create your models here.
class Bookmark(models.Model): #models.Model 상속
    site_name = models.CharField(max_length=100)
    url = models.URLField('Site URL')
    def __str__(self): #매직메서드&언더바메서드 : 클래스의 오브젝트를 출력할 때 나타날 내용을 결정
        return "이름 : " + self.site_name + ", 주소 : " + self.url
    def get_absolute_url(self): #작업 후 다시 돌아올 페이지
        return reverse('detail', args=[str(self.id)])