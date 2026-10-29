"""
URL configuration for config project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/6.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include
from rest_framework.routers import DefaultRouter
from club.views import MemberViewSet, DepartmentViewSet

# 引入 spectacular 的视图
from drf_spectacular.views import SpectacularAPIView, SpectacularSwaggerView

# 1. 注册 ModelViewSet 路由
router = DefaultRouter()
router.register(r'api/members', MemberViewSet)
router.register(r'api/departments', DepartmentViewSet)

admin.site.site_header = "信息化与商务智能协会管理后台"
admin.site.site_title = "信息化与商务智能协会管理后台"

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('club.urls')), # 社团管理

        # 2. 把 router 的接口路由包含进来
    path('', include(router.urls)),
    
    # 3. 配置文档路由（这就是你访问 /api/docs/ 的地方）
    path('api/schema/', SpectacularAPIView.as_view(), name='schema'),
    path('api/docs/', SpectacularSwaggerView.as_view(url_name='schema'), name='swagger-ui'),

]


from django.conf import settings
from django.conf.urls.static import static

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)