from django.urls import path

from . import views

urlpatterns = [
    path('index/', views.index),

    path('index/items/', views.items),
    path('index/items/add/', views.add_item),
    path('index/items/delete/<int:id>/', views.delete_item),
    path('index/items/update/<int:id>/', views.update_item),

    path('index/users/', views.users),
    path('index/users/add/', views.add_user),
    path('index/users/delete/<int:id>/', views.delete_user),
    path('index/users/update/<int:id>/', views.update_user),
]