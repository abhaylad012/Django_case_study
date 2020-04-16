from django.urls import path
from . import views

urlpatterns = [
    path('form', views.product_form, name='product_form'),
    path('view/<prod_id>', views.product_view, name='product_view'),
    path('delete/<prod_id>', views.product_delete, name='product_delete'),
    path('edit/<prod_id>', views.product_edit_form, name='product_edit_form'),
    path('update/<prod_id>', views.product_update, name='product_update')

]
