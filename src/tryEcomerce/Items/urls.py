from django.contrib import admin
from django.urls import path
from .views import create_Item_page, get_Items_list, item_detail, item_update, delete_Item, add_to_cart, cart_list_views


app_name = "Items"
urlpatterns = [

    path("", get_Items_list),
    path("create/", create_Item_page),
    path("<int:id>/", item_detail, name="detail"),
    path("up/<int:id>/", item_update, name="update"),
    path("delete/<int:id>/", delete_Item, name="delete"),
    path("add_to_cart/<int:id>/", add_to_cart),
    path("cart/", cart_list_views),

]
