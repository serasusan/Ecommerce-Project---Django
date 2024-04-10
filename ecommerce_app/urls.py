from django.urls import path
from . import views

urlpatterns = [
    path("",views.home,name="home"),
    path("product-list/",views.product_list,name="product_list"),
    path("product/<int:pk>/",views.product_detail,name="product_detail"),    
    path('create-product/', views.create_product, name='create_product'),
    path('update-product/<str:pk>/', views.update_product, name='update_product'),
    path('delete-product/<str:pk>/',views.deleteProduct,name='delete_product'),
    path('create-category/',views.createCategory,name='create_category'),
    path('update-category/<str:pk>/',views.updateCategory,name='update_category'),
    path('delete-category/<str:pk>/',views.deleteCategory,name='delete_category'),
    path('category-list/',views.category_list,name='category_list'),
    path('create-review/',views.createReview,name='create_review'),
    path('update-review/<str:pk>/',views.updateReview,name='update_review'),
]