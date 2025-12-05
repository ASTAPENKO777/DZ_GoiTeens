from django.shortcuts import render, get_object_or_404
from django.core.paginator import Paginator
from .models import Product

def product_list(request):
    products = Product.objects.all()
    
    paginator = Paginator(products, 4)
    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)
    
    return render(request, 'products/list.html', {
        'page_obj': page_obj,
        'products': page_obj.object_list,
    })

def product_detail(request, pk):
    product = get_object_or_404(Product, pk=pk)
    return render(request, 'products/detail.html', {'product': product})