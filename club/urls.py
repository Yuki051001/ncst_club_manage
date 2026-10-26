from . import views
from django.urls import path

urlpatterns = [
    path('api/members/',views.member_list, name='member_list'), # 获取所有成员信息
]