from django.contrib import admin
from django.urls import path, include
from blog.views import show_received_file  # 导入新的视图

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/', include('blog.urls')),  # 包含 blog 的 URL 配置
    path('show-received-file/', show_received_file, name='show_received_file'),  # 新增的路径
]
