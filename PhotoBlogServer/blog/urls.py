# blog/urls.py

from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import PhotoViewSet, show_received_file  # 导入新的视图

router = DefaultRouter()
router.register(r'photos', PhotoViewSet)  # 注册路由，路径为 'photos/'

urlpatterns = [
    path('', include(router.urls)),  # 包含现有的 API 路由
    path('show-received-file/', show_received_file, name='show_received_file'),  # 新增的路径
]
