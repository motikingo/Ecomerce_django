import enum
from msilib.schema import ListView
import numbers
from pydoc import describe
from statistics import mode
from tkinter import Widget
from xml.dom.minidom import Attr
import django
from django.db import models
from django.urls import reverse
from .Item_type import catagories


class Item(models.Model):
    catagory = models.CharField(max_length=100)
    name =  models.CharField(max_length=120)
    price  =  models.DecimalField(max_digits=10000, decimal_places=2)
    brand  =  models.CharField(max_length=120)
    describtion =  models.TextField()
    
    def Item_validation_detail(self):

        return reverse("Items:detail",kwargs={"id":self.id})

    def Item_validation_update(self):

        return reverse("Items:update",kwargs={"id":self.id})

    def Item_validation_delete(self):

        return reverse("Items:delete",kwargs={"id":self.id})



class Cart(models.Model):

    

    item_List =  []
    
    #name =  models.CharField(max_length=120 ) 
    #price  =  models.DecimalField(max_digits=10000, decimal_places=2) 
    #brand  =  models.CharField(max_length=120)
    #number_of_order = models.IntegerField()

    def add_to_cart(self,id_for_item):
        return reverse("Item:cart",kwargs={id:id_for_item})
