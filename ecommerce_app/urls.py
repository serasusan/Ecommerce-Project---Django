from django.urls import path
from . import views

urlpatterns = [
    path("",views.product_list,name="product_list"),
    # path("",views.test,name="test")
    path("product/<int:pk>/",views.product_detail,name="product_detail"),    
]