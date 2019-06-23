from django.urls import path
from .views import *

urlpatterns = [
    path('', BookmarkListView.as_view(), name='list'), #북마크앱의 루트페이지, 클래스형 뷰일경우 as_view()붙이기
    path('add/', BookmarkCreateView.as_view(), name='add'),
    path('detail/<int:pk>/', BookmarkDetailView.as_view(), name='detail'),
    #<컨버터:컨버터를 통해 반환받은 값 혹은 패턴에 일치하는 값의 변수명>
    #str : 비어있지 않은 모든 문자와 매칭 '/'미포함
    #int : 0을포함한 양의 정수와 매칭
    #slug : 아스키 문자나 숫자, 하이픈, 언더스코어를 포함한 슬러그 문자열과 매칭
    #uuid : UUID와 매칭
    #path : /포함 str
    path('update/<int:pk>/', BookmarkUpdateView.as_view(), name='update'),
    path('delete/<int:pk>/', BookmarkDeleteView.as_view(), name='delete'),
]