from django.urls import path

from . import views

urlpatterns = [
    path('', views.index),

    path('items/<int:id>/', views.items),
    path('items/add/', views.add_item),
    path('items/delete/<int:id>/', views.delete_item),
    path('items/update/<int:id>/', views.update_item),

    path('items/traitement_add_item', views.traitement_add_item),

    path('users/', views.users),
    path('users/add/', views.add_user),
    path('users/delete/<int:id>/', views.delete_user),
    path('users/update/<int:id>/', views.update_user),
]