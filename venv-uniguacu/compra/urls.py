from django.urls import path
from . import views

urlpatterns = [
    path('', views.index_compra, name='index_compra'),
    path('<int:id>/', views.view_compra, name='view_compra'),
    path('edit/<int:id>/', views.edit_compra, name='edit_compra'),
    path('add/', views.add_compra, name='add_compra'),
    path('delete/<int:id>', views.delete_compra, name='delete_compra'),
    path('pdf/<int:id>', views.pdf_compra, name='pdf_compra'),
]