from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('products', views.products, name='indexproducts'),
    path('products/upsert', views.upsertProducts, name='upsertproducts'),
    path('products/upsert/<int:id_product>', views.upsertProducts, name='upsertproducts'),
    path('products/delete', views.deleteProducts, name='deleteproducts'),
    path('products/delete/<int:id_product>', views.deleteProducts, name='deleteproducts'),
]