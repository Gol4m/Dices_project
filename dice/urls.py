from django.urls import path
from . import views

urlpatterns = [
    path('', views.get_main_page, name='main-page'),
    path('mulri-throw', views.get_multi_throw, name='multi-throw'),
    path('<str:dice_n>', views.get_info_dice, name='dice-page'),
    path('roll/<str:dice_n>/', views.roll_dice_ajax, name='roll-dice-ajax'),
    path('multi-roll/', views.roll_multi_dice, name='roll-multi-dice'),  # Новый URL для мульти-броска
]