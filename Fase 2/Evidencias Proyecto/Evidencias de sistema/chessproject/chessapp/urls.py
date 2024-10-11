from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),  
    path('login/', views.login_view, name='login'),
    path('menu/', views.menu, name='menu'),
    path('signin/', views.signin, name='signin'),
    path('tablero/', views.tablero, name='tablero'),
    path('logout/', views.logout_view, name='logout'),
    path('partidas-en-vivo/', views.partidas_en_vivo, name='partidas_en_vivo'),
    path('tutoriales/', views.tutoriales, name='tutoriales'),
    path('estadisticas/', views.estadisticas_view, name='estadisticas'),
    path('contacto/', views.contacto, name='contacto'),
    path('configuracion/', views.configuracion, name='configuracion'),
]
# 