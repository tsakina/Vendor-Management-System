from vendors.models import PurchaseOrder, HistoricalPerformance
from django.db.models.signals import post_save
from django.dispatch import receiver
from django.db.models import Avg
from datetime import timedelta

def on_time_delivery_metrics(vendor_id, delivery_date):
    
    """This function calculates the On-Time Delivery Rate 
    and the corresponding signal handle_po_status_change to trigger this function 
    everytime there is a change in Purchase Order Status"""

    # Count completed POs delivered on or before delivery_date
    completed_poss = PurchaseOrder.objects.filter(
        vendor_id=vendor_id,
        status='completed',
        delivery_date=str(delivery_date)
    ).count()

    # Count total completed POs for the vendor
    total_completed_poss = PurchaseOrder.objects.filter(
        vendor_id=vendor_id,
        status='completed'
    ).count()

    # Calculate the metric (avoid division by zero)
    metric = 0.0
    if total_completed_poss > 0:
        metric = completed_poss / total_completed_poss

    performance = HistoricalPerformance.objects.get(vendor=vendor_id)
    performance.on_time_delivery_rate = metric
    performance.save()

def calculate_quality_rating_average(vendor):
    """This function calculates the Quality Rating Average
    and the corresponding signal handle_po_status_change to trigger this function 
    everytime there is a change in Purchase Order Status"""

    # Assuming you have a PurchaseOrder model with a quality_rating field
    completed_pos = PurchaseOrder.objects.filter(vendor=vendor, status="complete")
    for pos in completed_pos:
        if pos.quality_rating == None:
            pass

    average_rating = completed_pos.aggregate(avg_quality_rating=Avg("quality_rating"))
    quality_rating_metrics = HistoricalPerformance(
        vendor=vendor,
        quality_rating_avg=average_rating
    )
    quality_rating_metrics.save()

def calculate_average_response_time(vendor):
    """This function calculates the Average Response Time 
    the corresponding signal handle_po_status_change to trigger this function 
    everytime there is a change in Purchase Order Status"""

    purchase_orders = PurchaseOrder.objects.filter(vendor=vendor)
    total_time = timedelta(seconds=0)
    num_orders = len(purchase_orders)

    for order in purchase_orders:
        time_diff = order.acknowledgment_date - order.issue_date
        total_time += time_diff

    if num_orders > 0:
        average_time = total_time / num_orders
        average_response_time_metrics = HistoricalPerformance(
            vendor=vendor,
            average_response_time=average_time
        )
        average_response_time_metrics.save()
    else:
        pass

def calculate_fulfillment_rate(vendor):
    """This function calculates the Fulfillment Rate 
    and the corresponding signal handle_po_status_change to trigger this function 
    everytime there is a change in Purchase Order Status"""
    completed_pos = PurchaseOrder.objects.filter(vendor=vendor, status="completed")
    total_pos = PurchaseOrder.objects.filter(vendor=vendor)
    
    if total_pos.exists():
        fulfillment_rate = (completed_pos.count() / total_pos.count()) * 100
    else:
        fulfillment_rate = 0.0  # Handle the case when no POs exist for the vendor
    
    fulfillment_rate_metrics = HistoricalPerformance(
        vendor=vendor,
        fulfillment_rate=fulfillment_rate
    )
    fulfillment_rate_metrics.save()

@receiver(post_save, sender=PurchaseOrder)
def handle_po_status_change(sender, instance, **kwargs):
    if instance.status == 'complete':
        on_time_delivery_metrics(sender.vendor, str(sender.delivery_date).strip("TZ"))
        calculate_quality_rating_average(sender.vendor)
        calculate_fulfillment_rate(sender.vendor)

@receiver(post_save, sender=PurchaseOrder)
def handle_acknowledge_date(sender, instance, **kwargs):
    if instance.acknowledgment_date != None:
        calculate_fulfillment_rate(sender.vendor)

