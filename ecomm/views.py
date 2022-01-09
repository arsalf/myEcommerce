from django.shortcuts import render
from django.http import HttpResponse
from ecomm.models import product
from ecomm.models import keranjang
from django.shortcuts import redirect

# Create your views here.
def index(request):
    data_product = product.objects.all()
    data_keranjang = keranjang.objects.all()
    return render(request, 'index.html', {'products': data_product, 'keranjang':data_keranjang})

def add(request):
    if request.method == 'POST':
        data = keranjang(id_produk=request.POST.get('id_product'), jmlh=1)
        data.save()
    
    return redirect('/')    

def delete(request):
    if request.method == 'POST':
        data = keranjang.objects.get(id_produk=request.POST.get('id_product'))
        data.delete()
    
    return redirect('/')