from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),  # 首页
    path('crops/<str:crop_name>/', views.crops_info, name='crops_info'),  # 模型信息
]
