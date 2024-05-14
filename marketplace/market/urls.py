from django.urls import path

from . import views

urlpatterns = [
    path('', views.index),

    path('login/', views.login),
    path('login/login_user/', views.login_user),
    path('logout/', views.logout),

    path('items/<int:id>/', views.items),
    path('items/add/', views.add_item),
    path('items/delete/<int:id>/', views.delete_item),
    path('items/update/<int:id>/', views.update_item),

    path('items/traitement_add_item', views.traitement_add_item),
    path('items/buy/<int:id>/', views.buy_item),

    path('users/<int:id>/', views.users),
    path('users/add/', views.add_user),
    path('users/delete/<int:id>/', views.delete_user),
    path('users/update/<int:id>/', views.update_user),

    path('users/traitement_add_user', views.traitement_add_user),
]