from django.contrib import admin
from django.urls import path, include
from .views import search, dashboard

urlpatterns = [
    path('', dashboard, name='dashboard'),
    path('admin/', admin.site.urls),
    path('fornecedor/', include('fornecedor.urls')),  
    path('item/', include('item.urls')),  
    path('requisicao/', include('requisicao.urls')),  
    path('search/', search, name='search'),
    path('dashboard/', dashboard, name='dashboard'),
    path('compra/', include('compra.urls')),
    path('veiculo/', include('veiculo.urls')),
]


