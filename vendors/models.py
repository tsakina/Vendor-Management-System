from django.db import models


# Create your models here.
class Vendor(models.Model):
    name = models.CharField(max_length=100, unique=True)
    contact_details = models.TextField()
    address = models.TextField()
    vendor_code = models.CharField(max_length=100, unique=True)
    on_time_delivery_rate = models.FloatField(max_length=100)
    quality_rating_avg = models.FloatField(max_length=100)
    average_response_time = models.FloatField(max_length=100)
    fulfillment_rate = models.FloatField(max_length=100)

    def __str__(self) -> str:
        return self.name

class PurchaseOrder(models.Model):
    po_number = models.CharField(max_length=50, unique=True)
    vendor = models.ForeignKey(Vendor, on_delete=models.CASCADE)
    order_date = models.DateTimeField(auto_now_add=True)  #-Date when the order was placed.
    delivery_date = models.DateTimeField()  #- Expected or actual delivery date of the order.
    items = models.JSONField()   #- Details of items ordered.
    quantity = models.IntegerField()    #- Total quantity of items in the PO.
    status = models.CharField(max_length=100)  #- Current status of the PO (e.g., pending, completed, canceled).
    quality_rating = models.FloatField(null=True)  #- Rating given to the vendor for this PO (nullable).
    issue_date = models.DateTimeField()   #- Timestamp when the PO was issued to the vendor.
    acknowledgment_date = models.DateTimeField(null=True)  #- nullable - Timestamp when the vendor acknowledged the PO.


class HistoricalPerformance(models.Model):
    vendor = models.ForeignKey(Vendor, on_delete=models.CASCADE)  #- Link to the Vendor model.
    date = models.DateTimeField(auto_now_add=True,) #- Date of the performance record.
    on_time_delivery_rate = models.FloatField()  #- Historical record of the on-time delivery rate.
    quality_rating_avg = models.FloatField()  #- Historical record of the quality rating average.
    average_response_time = models.FloatField()  #- Historical record of the average response time.
    fulfillment_rate = models.FloatField()  #- Historical record of the fulfilment rate.
