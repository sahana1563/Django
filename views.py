from django.shortcuts import render, get_object_or_404, redirect, HttpResponseRedirect
from .forms import ProductForm
from .models import category, product, review
from django.core.paginator import Paginator
from django.contrib.auth.decorators import login_required, permission_required
from django.views.decorators.csrf import csrf_exempt
# Create your views here.

@csrf_exempt
def product_create(request):
    context = {}
    form = ProductForm(request.POST or None)
    if form.is_valid():
        form.save()
    context['form'] = form
    return render(request, "shop/product_form.html", context)
@csrf_exempt
def products_list(request):
    product_list = product.objects.all()
    paginator = Paginator(product_list, 10)
    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)
    return render(request, 'shop/product_list.html', {'page_obj': page_obj})
@csrf_exempt
def product_detail(request, id):
    product_req = get_object_or_404(product, id=id)
    return render(request, 'shop/product_detail.html', {'product_req': product_req})
@csrf_exempt
def product_update(request, id):
    context = {}
    product_req = get_object_or_404(product, id = id)
    form = ProductForm(request.POST or None, instance = product_req)
    if form.is_valid():
        form.save()
        return HttpResponseRedirect("/products/"+ id+"/detail/")
    context["form"] = form
    return render(request, "shop/product_form.html", context)
@csrf_exempt
def product_delete(request, id):
    product_req = get_object_or_404(product,id=id)
    if request.method == 'POST':
        product_req.delete()
        return redirect('products_list')
    return render(request, 'shop/product_confirm_delete.html', {'product_req': product_req})   
    
@csrf_exempt
def categories_list(request):
    category_list = category.objects.all()
    return render(request, 'shop/categories_list.html', {'category_list': category_list})
