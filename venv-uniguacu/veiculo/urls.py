from django.urls import path
from . import views

urlpatterns = [
    path('', views.index_veiculo, name='index_veiculo'),
    path('<int:id>/', views.view_veiculo, name='view_veiculo'),
    #path('edit/<int:id>/', views.edit_veiculo, name='edit_veiculo'),
    path('veiculo/edit/<int:veiculo_id>/', views.edit_veiculo, name='edit_veiculo'),
    path('add/', views.add_veiculo, name='add_veiculo'),
    path('delete/<int:veiculo_id>', views.delete_veiculo, name='delete_veiculo'),
    path('pdf/<int:veiculo_id>', views.pdf_veiculo, name='pdf_veiculo'),

    
]