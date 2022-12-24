from django.urls import path

from productsApp.views import create_products, list_products, list_categories, create_category


urlpatterns = [
    path('create-product/', create_products),
    path('list-products/', list_products),

    path('create-category/<str:name>/', create_category),
    path('list-categories/', list_categories),
]