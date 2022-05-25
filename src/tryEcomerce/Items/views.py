from asyncio.windows_events import NULL

from urllib import request
from django.shortcuts import render, get_object_or_404, redirect

from .form import ItemsForm, CartForm
from .models import Item, Cart
from django.core import serializers


def create_Item_page(request):
    form = ItemsForm(request.POST or None)

    if form.is_valid():
        Item.objects.create(**form.cleaned_data)
        form.save()
        form = ItemsForm()

    return render(request, "Items/create_Item.html", {"form": form})



cart_id = -1

def get_Items_list(request):
    queryset = Item.objects.all()
    cart = Cart.objects.create()
    global cart_id
    #if Cart.objects.all() != NULL:

    # for cart in Cart.objects.all():
    #    cart.delete()

    if "cart" not in request.session:
        #for cart in Cart.objects.all():
        #    cart.delete()
       
        
        cart
        cart_id = cart.id
        request.session["cart"] = serializers.serialize("json",Cart.objects.all())
        
        #cart_obj_try = get_object_or_404(Cart, id=1)

    print(cart)
    return render(request, "Items/item_list.html", {
        "objects_list": queryset,
        #"cart": serializers.deserialize('json',request.session["cart"])


    })


def count(x):
    return 

def item_detail(request, id):
    obj = get_object_or_404(Item, id=id)

    return render(request, "Items/item_detail.html", {"obj": obj})


def item_update(request, id):
    obj = get_object_or_404(Item, id=id)

    form = ItemsForm(request.POST or None, instance=obj)

    if form.is_valid():

        form.save()

        return redirect("../../")

    return render(request, "Items/create_Item.html", {"form": form})


def delete_Item(request, id):
    obj = get_object_or_404(Item, id=id)

    if request.method == "POST":
        obj.delete()
        return redirect("../../")
    return render(request, "Items/delete_item.html", {"obj": obj})



def add_to_cart(request, id):

    cart_obj = get_object_or_404(Item, id=id)

    cart_instance = {"name": cart_obj.name, "price": cart_obj.price,
                     "brand": cart_obj.brand, "number_of_order": 0}
    cart_form = CartForm(request.POST or None, initial=cart_instance)

    #cart_form.name = cart_obj.name
    #cart_form.brand = cart_obj.brand
    #cart_form.price = cart_obj.price
    #cart_form.number_of_order = NULL

    if cart_form.is_valid():
        # Cart.  (cart_obj)
        #if not cart_id==-1:

        cart_list =list (serializers.deserialize ("json", request.session["cart"])) 

        Cart(cart_list[cart_id]).item_List.append(cart_instance)
    

        print(cart_list)
        return redirect("../../")

    return render(request, "Cart/add_to_cart.html", {"cart_form": cart_form})


def cart_list_views(request):
    #object_in_cart = get_object_or_404(Cart, id=1)
    #if not cart_id==-1:

    cart_list = list(serializers.deserialize("json", request.session["cart"]))
   # print(queryset)

    return render(request, "Cart/list_order.html", {"queryset":Cart(cart_list[cart_id]).item_List})

    #return("Not cart object exist!")
