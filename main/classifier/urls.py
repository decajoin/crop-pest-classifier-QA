from django.urls import path
from . import views

urlpatterns = [
    path('classify/', views.classify, name='classify'),  # 图像分类功能
]
