from django.urls import path
from . import views

urlpatterns = [
    path('', views.index_item, name='index_item'),
    path('<int:id>/', views.view_item, name='view_item'),
    path('edit/<int:id>/', views.edit_item, name='edit_item'),
    path('add/', views.add_item, name='add_item'),
    path('delete/<int:id>', views.delete_item, name='delete_item'),
]
