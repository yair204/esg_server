from django.urls import path
from . import views

urlpatterns = [
    path('items/', views.products, name='items'),
    path('upload_img/',views.product_image_view ,name='upload_img'),
]