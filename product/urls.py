from django.urls import path
from .views import ProductList , ProductDetail,ProductCreate,ProductUpdate

urlpatterns = [
    path('',ProductList.as_view(),name='home'),
    path('create',ProductCreate.as_view(),name='create'),
    path('dateil/<int:pk>',ProductDetail.as_view(),name='dateil'),
    path('update/<int:pk>', ProductUpdate.as_view(), name='update'),
]