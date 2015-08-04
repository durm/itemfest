from django.shortcuts import render, render_to_response
from models import Product

def product_view(request, product_id):
	try:
		product = Product.objects.get(id=product_id)
	except Product.DoesNotExist:
		product = None
	return render_to_response("products/product.html", {"product": product, "product_id": product_id})