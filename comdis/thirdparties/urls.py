from django.urls import path
from . import views


urlpatterns = [
    path('', views.index, name='indexthirdparties'),
    path('upsertClient', views.upsertClients, name='upsertclient'),
    path('upsertClient/<int:id_client>', views.upsertClients, name='upsertclient'),
    path('upsertSupplier', views.upsertSupplier, name='upsertsupplier'),
    path('upsertSupplier/<int:id_supplier>', views.upsertSupplier, name='upsertsupplier'),
    path('deleteClient', views.deleteclient ,name='deleteclient'),
    path('deleteClient/<int:id_client>', views.deleteclient, name='deleteclient'),
    path('deleteSupplier', views.deletesupplier, name='deletesupplier'),
    path('deleteSupplier/<int:id_supplier>', views.deletesupplier, name='deletesupplier'),
    
]