from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('add_book/', views.add_book, name='add_book'),
    path('reading_list/', views.reading_list, name='reading_list'),
    path('add_to_reading_list/<int:book_id>/', views.add_to_reading_list, name='add_to_reading_list'),
    path('mark_as_read/<int:book_id>/', views.mark_as_read, name='mark_as_read'),
    path('mark_as_to_read/<int:book_id>/', views.mark_as_to_read, name='mark_as_to_read'),
    path('friends/', views.friends, name='friends'),
    path('add_friend/', views.add_friend, name='add_friend'),
    path('friend_reading_list/<int:user_id>/', views.friend_reading_list, name='friend_reading_list'),
]
