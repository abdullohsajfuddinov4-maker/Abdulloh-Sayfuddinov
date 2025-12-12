from django.shortcuts import render ,redirect
from django.urls import reverse_lazy
from django.views import View
from .models import Product , Category
from .forms import ProductForm
from django.shortcuts import get_object_or_404

# Create your views here.

class ProductList(View):
    def get(self,request):
        product = Product.objects.all().order_by('-id')
        context = {'product':product}
        return render(request,'home.html',context)


class ProductDetail(View):
    def get(self,request,pk):
        product = get_object_or_404(Product,pk=pk)
        context = {'product':product}
        return render(request,'dateil.html',context)


