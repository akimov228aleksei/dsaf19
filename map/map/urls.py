from django.contrib import admin
from django.urls import path
from point import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.point),
    path('points_list', views.save_point),
]