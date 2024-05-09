from django.test import TestCase
from vendors.models import *

# Create your tests here.
class VendorTestCase(TestCase):

    def setup(self):
    
        Vendor.objects.create(
            name = "Amazon",
            contact_details = "California, USA",
            address = "California, USA",
            vendor_code = "001",
            on_time_delivery_rate = 80.5,
            quality_rating_avg = 99.1,
            average_response_time = 87.7,
            fulfillment_rate = 99.9
        )

