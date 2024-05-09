from django.urls import path
from vendors.views import *

urlpatterns = [
    path('vendors/', get_create_vendor),
    path('vendors/<int:id>', update_delete_vendor),

    path('purchase_orders/', get_create_po),
    path('purchase_orders/<int:id>', update_delete_po),

    path('purchase_orders/<int:id>/acknowledge', update_po_acknowledge_date),

    path('vendors/<int:id>/performance', get_vendor_performance),
]