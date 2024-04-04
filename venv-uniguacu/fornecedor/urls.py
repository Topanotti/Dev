from django.urls import path
from . import views

urlpatterns = [
    path('', views.index_fornecedor, name='index_fornecedor'),
    path('<int:id>/', views.view_fornecedor, name='view_fornecedor'),
    path('edit/<int:id>/', views.edit_fornecedor, name='edit_fornecedor'),
    path('add/', views.add_fornecedor, name='add_fornecedor'),
    path('delete/<int:id>', views.delete_fornecedor, name='delete_fornecedor'),
]
