from django.urls import path
from . import views

urlpatterns = [
    path('', views.get_main_page, name='main-page'),
    path('<str:dice_n>', views.get_info_dice, name='dice-page'),
    path('roll/<str:dice_n>/', views.roll_dice_ajax, name='roll-dice-ajax'),

]