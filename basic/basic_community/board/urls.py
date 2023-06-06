from django.urls import path
from . import views

urlpatterns = [
    path('detail/<int:pk>', views.board_detail),
    path('list/', views.board_list),
    path('writer/', views.board_writer)
]
