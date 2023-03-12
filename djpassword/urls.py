from django.contrib import admin
from django.urls import path
from generator import views

urlpatterns = [
    #path('admin/', admin.site.urls),
    path('portfolio/', views.portfolio, name='portfolio'),
    path('', views.index, name='index'),
    path('password', views.password, name='password')

]
