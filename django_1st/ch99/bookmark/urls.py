from django.urls import path
from bookmark.views import BookmarkLV, BookmarkDV
from bookmark.views import BookmarkCreateView, BookmarkChangeLV
from bookmark.views import BookmarkUpdateView, BookmarkDeleteView

"""
위의 import에서 bookmark.views가 아니라 bookmark 자체를 import한 후 views.[클래스명]을 사용하는 형식을 해도 됨
import할 대상이 많다면 위와 같이 모듈을 관리하는 것이 하나의 방법임
"""

app_name = 'bookmark'

urlpatterns = [
    path('', BookmarkLV.as_view(), name = 'index'),
    path('<int:pk>/', BookmarkDV.as_view(), name = 'detail'),
    path('add/', BookmarkCreateView.as_view(), name='add'),
    path('change/', BookmarkChangeLV.as_view(), name='change'),
    path('<int:pk>/update/', BookmarkUpdateView.as_view(), name='update'),
    path('<int:pk>/delete/', BookmarkDeleteView.as_view(), name='delete'),
]