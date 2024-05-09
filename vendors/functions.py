from rest_framework.response import Response
from rest_framework import status

def check_object_availability(any_model, id):
    try:
        object = any_model.objects.get(id = id)
    except any_model.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)    
    return object
    
def valid_serializer(model_serializer):
    if model_serializer.is_valid():
        model_serializer.save()
        return Response(model_serializer.data, status=status.HTTP_201_CREATED)
    return Response(model_serializer.errors)

# views.py or wherever you handle this logic

from django.db.models import Count, F, FloatField, ExpressionWrapper

# # Example usage:
# vendor_id = 1  # Replace with the actual vendor ID
# delivery_date = '2024-05-07'  # Replace with the desired date
# metric_value = calculate_metric(vendor_id, delivery_date)
