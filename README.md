# Vendor-Management-System

This is a project in progess.

This project is a Vendor Management System using Django and Django REST Framework. This system will handle vendor profiles, track purchase orders, and calculate vendor performance metrics.

To install the packages run the following command in the terminal of the IDE is being used -

- pip install -r requirements.txt

After all the packages are installed, run the following command to create database migrations :- 

- python manage.py makemigrations
  
To create tables in the database :-

- python manage.py migrate

And finally to run the project on a local host :-

- python manage.py runserver

** Postman or localhost can be used to test the project API's.

** Run the tests.py file to check the functionality and reliability of the endpoints:-

-- ./manage.py test

Documentation on Vendor Management System API's:-

All API's are token-based authenticated and can be accessed by the following token:-

In the headers pass:

- Authorization: Token 690d667276613a5b05b29923a0cf56774a6d2491 

Vendor Profile Management:

A model to store vendor information including name, contact
details, address, and a unique vendor code.

API Endpoints:

- POST /api/vendors/: Creates a new vendor.

- GET /api/vendors/: Lists all the vendors.

- GET /api/vendors/{vendor_id}/: Retrieves a specific vendor's details by providing that particular vendors id.

- PUT /api/vendors/{vendor_id}/: Updates a vendor's details by providing that particular vendors id.

- DELETE /api/vendors/{vendor_id}/: Delete a vendor by providing that particular vendors id.


Purchase Order Tracking:

Track purchase orders with fields like PO number, vendor reference,
order date, items, quantity, and status.

API Endpoints:

- POST /api/purchase_orders/: Creates a purchase order.

- GET /api/purchase_orders/: List all purchase orders with an option to filter by
vendor.

- GET /api/purchase_orders/{po_id}/: Retrieve details of a specific purchase order by providing that particular purchase order id.

- PUT /api/purchase_orders/{po_id}/: Update a purchase order by providing that particular purchase order id.

- DELETE /api/purchase_orders/{po_id}/: Delete a purchase order by providing that particular purchase order id.

Vendor Performance Evaluation:

Metrics:

- On-Time Delivery Rate: Percentage of orders delivered by the promised date.

- Quality Rating: Average of quality ratings given to a vendor’s purchase orders.

- Response Time: Average time taken by a vendor to acknowledge or respond to
purchase orders.

- Fulfilment Rate: Percentage of purchase orders fulfilled without issues.

- Model Design: Add fields to the vendor model to store these performance metrics.

API Endpoints:

Retrieves the calculated performance metrics for a specific vendor.
Should return data including on_time_delivery_rate, quality_rating_avg,
average_response_time, and fulfillment_rate.

- GET /api/vendors/{vendor_id}/performance: Retrieve a vendor's performance
metrics.


Update Acknowledgment Endpoint:

- POST /api/purchase_orders/{po_id}/acknowledge - for vendors to acknowledge
purchase order
This endpoint will update acknowledgment_date and trigger the recalculation
of average_response_time.


