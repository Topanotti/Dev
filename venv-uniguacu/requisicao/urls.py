from django.urls import path
from . import views


urlpatterns = [
    path('', views.index_requisicao, name='index_requisicao'),
    path('<int:id>/', views.view_requisicao, name='view_requisicao'),
    path('edit/<int:id>/', views.edit_requisicao, name='edit_requisicao'),
    path('add/', views.add_requisicao, name='add_requisicao'),
    path('delete/<int:id>', views.delete_requisicao, name='delete_requisicao'),
    path('pdf/<int:id>', views.pdf_requisicao, name='pdf_requisicao')
    
]
