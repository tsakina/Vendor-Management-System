from rest_framework.decorators import api_view, authentication_classes, permission_classes
from rest_framework.response import Response
from rest_framework.authentication import TokenAuthentication
from rest_framework.permissions import IsAuthenticated
from rest_framework import status
from vendors.models import *
from vendors.serializers import *
from vendors.functions import *

"""
* All Views Requires token authentication.
* Only admin users are able to access the view.
"""

# Username : admin
# Email address: admin@email.com  
# token = Token 690d667276613a5b05b29923a0cf56774a6d2491
    
# Create your views here.
@api_view(['GET', 'POST'])
@authentication_classes([TokenAuthentication])
@permission_classes([IsAuthenticated])
def get_create_vendor(request):
    if request.method == 'GET':
        queryset = Vendor.objects.all()
        serializer = VendorSerializer(queryset, many=True)

        return Response(serializer.data)
    
    elif request.method == 'POST':
        data = request.data
        serializer = VendorSerializer(data=data)
        serializer_validation = valid_serializer(serializer)
        return serializer_validation
        # if serializer.is_valid():
        #     serializer.save()
        #     return Response(serializer.data, status=status.HTTP_201_CREATED)
        # return Response(serializer.errors)

@api_view(['GET', 'PUT', 'DELETE'])
def update_delete_vendor(request, id):

    data = request.data

    try:
        vendor = Vendor.objects.get(id = id)
    except Vendor.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)

    if request.method == 'GET':        
        serializer = VendorSerializer(vendor, many=False)
        return Response(serializer.data)
            
    elif request.method == 'PUT':        
        serializer = VendorSerializer(vendor, data=data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_202_ACCEPTED)
        return Response(serializer.errors)
    
    elif request.method == 'DELETE':
        vendor.delete()
        return Response({'message': f'{vendor.name} deleted'}, status=status.HTTP_204_NO_CONTENT)
    
@api_view(['GET', 'POST'])
def get_create_po(request):
    if request.method == 'GET':
        queryset = PurchaseOrder.objects.all()
        serializer = PurchaseOrderSerializer(queryset, many=True)

        return Response(serializer.data)
    
    elif request.method == 'POST':
        data = request.data
        serializer = PurchaseOrderSerializer(data=data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors)

@api_view(['GET', 'PUT', 'DELETE'])
def update_delete_po(request, id):

    data = request.data
    purchase_order = check_object_availability(PurchaseOrder, id)

    # try:
    #     purchase_order = PurchaseOrder.objects.get(id = id)
    # except PurchaseOrder.DoesNotExist:
    #     return Response(status=status.HTTP_404_NOT_FOUND)

    if request.method == 'GET':        
        serializer = PurchaseOrderSerializer(purchase_order, many=False)
        return Response(serializer.data)
            
    elif request.method == 'PUT':        
        serializer = PurchaseOrderSerializer(purchase_order, data=data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_202_ACCEPTED)
        return Response(serializer.errors)
    
    elif request.method == 'DELETE':
        purchase_order.delete()
        return Response({'message': 'Purchase Order deleted'}, status=status.HTTP_204_NO_CONTENT)

@api_view(['PUT'])
def update_po_acknowledge_date(request, id):
    data = request.data

    try:
        update_po = PurchaseOrder.objects.get(id=id)
    except PurchaseOrder.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)
    
    if request.method == 'PUT':
        serializer = PurchaseOrderSerializer(update_po, data=data, many=False)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_202_ACCEPTED)
        return Response(serializer.errors)


@api_view(['GET'])
def get_vendor_performance(request, id):
    data = request.data

    try:
        performance_metrix = HistoricalPerformance.objects.get(id=id)
    except HistoricalPerformance.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)
    
    if request.method == 'GET':
        serializer = HistoricalPerformanceSerializer(performance_metrix, data=data, many=False)
        return Response(serializer.data)
