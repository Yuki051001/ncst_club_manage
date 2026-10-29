# from . import views
# from django.urls import path

# urlpatterns = [
#     path('api/members/',views.member_list, name='member_list'), # 获取所有成员信息
# ]


from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import MemberViewSet, DepartmentViewSet, CompetitionViewSet

# 实例化路由器
router = DefaultRouter()

# 注册路由：前端请求 /api/members/ 就会自动分配给 MemberViewSet
router.register(r'api/members', MemberViewSet)
router.register(r'api/departments', DepartmentViewSet)
router.register(r'api/competitions', CompetitionViewSet)

urlpatterns = [
    # 把路由器生成的路由全部包含进来
    path('', include(router.urls)),
]