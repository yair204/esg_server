from django.http import HttpResponse
from django.template import loader
from django.shortcuts import render, redirect
from .models import Product
from .form import ProductForm 


def products(request):
    products_data = [
        {
            "name": "Product 1",
            "title": "Title 1",
            "amount": 10.99,
            "location": "Location 1",
            "description": "Description 1",
        },
        {
            "name": "Product 2",
            "title": "Title 2",
            "amount": 20.99,
            "location": "Location 2",
            "description": "Description 2",
        },
        {
            "name": "Product 3",
            "title": "Title 3",
            "amount": 30.99,
            "location": "Location 3",
            "description": "Description 3",
        },
    ]

    for data in products_data:
        product = Product(**data)
        product.save()
    myproduct = Product.objects.all().values()
    template = loader.get_template("all_products.html")
    context = {
        "myproduct": myproduct,
    }

    return HttpResponse(template.render(context, request))

def product_image_view(request):
 
    if request.method == 'POST':
        form = ProductForm(request.POST, request.FILES)
 
        if form.is_valid():
            form.save()
            return redirect('success')
    else:
        form = ProductForm()
    return render(request, 'all_products.html', {'form': form})
 
 
def success(request):
    return HttpResponse('successfully uploaded')