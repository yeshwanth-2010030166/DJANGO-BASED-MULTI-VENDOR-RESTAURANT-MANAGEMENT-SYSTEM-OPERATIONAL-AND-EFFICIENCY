from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),

    path('user_login', views.user_login, name='user_login'),
    path('user_allfood', views.user_allfood, name='user_allfood'),
    path('book_table', views.book_table, name='book_table'),
    path('user_bookings', views.user_bookings, name='user_bookings'),

    path('seller_login', views.seller_login, name='seller_login'),
    path('seller_addre', views.seller_addre, name='seller_addre'),
    path('seller_addres', views.seller_addres, name='seller_addres'),
    path('seller_addfoods', views.seller_addfoods, name='seller_addfoods'),
    path('seller_bookings', views.seller_bookings, name='seller_bookings'),
    path('seller_updatebookings', views.seller_updatebookings, name='seller_updatebookings'),
    path('seller_updatebookingsss', views.seller_updatebookingsss, name='seller_updatebookingsss'),

    path('register', views.register, name='register'),
]