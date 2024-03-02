from django.urls import path

from . import views

urlpatterns = [
    path('', views.index, name='main_menu'),
    path('<path:path>/', views.draw_menu, name='draw_menu'),
]