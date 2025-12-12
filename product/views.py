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


class ProductCreate(View):
    def get(self,request):
        form = ProductForm()
        context = {'form':form}
        return render(request,'create.html',context)

    def post(self,request):
        form = ProductForm(request.POST,request.FILES)
        if form.is_valid():
            form.save()
            return redirect('home')
        return render(request, 'create.html', context={'form':form})


class ProductUpdate(View):
    def get(self,request,pk):
        product = get_object_or_404(Product,pk=pk)
        form = ProductForm(instance=product)

        context = {'form':form}
        return render(request,'update.html',context)

    def post(self,request,pk):
        product = get_object_or_404(Product, pk=pk)
        form = ProductForm(request.POST,request.FILES,instance=product)
        if form.is_valid():
            form.save()
            return redirect('home')
        return render(request, 'create.html', context={'form':form})


class ProductDelete(View):
    def get(self, request, pk):
        product = get_object_or_404(Product, pk=pk)
        context = {'product': product}
        return render(request, 'delete.html', context)

    def post(self, request, pk):
        product = get_object_or_404(Product, pk=pk)
        product.delete()
        return redirect('home')





