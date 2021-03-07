from django.urls import path
from . import views


urlpatterns = [
    path('', views.products, name='indexproducts'),
    path('upsert', views.upsertProducts, name='upsertproducts'),
    path('upsert/<int:id_product>', views.upsertProducts, name='upsertproducts'),
    path('delete', views.deleteProducts, name='deleteproducts'),
    path('delete/<int:id_product>', views.deleteProducts, name='deleteproducts'),
]