# PhotoBlogServer/urls.py

from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/', include('blog.urls')),  # 包含 blog 的 URL 配置
]
