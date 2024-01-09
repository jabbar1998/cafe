from django.shortcuts import render
from django.db import connection
from django.views import View
from order.models import Order, Table, OrderItem
import math 
import numpy as np
import pandas as pd
from datetime import datetime


class PopularProduct(View):
    ordered_products = []
    most_ordered = None
    for product in OrderItem.product:
        ordered_products.append(product)
    all_products = {ordered_products}
    dic = dict()
    for i in all_products:
        count = ordered_products.count(i)
        dic.update({i : count})
        
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.highest = max([eval(i) for i in self.dic.keys()])
        self.res = [item for item, value in self.dic.items() if value == self.highest]
        
    def get(self, request):
        return render(request, {'result': self.res})
        
        
class Peak_hour(View):
   
    all_hours = [date.strftime("%H") for date in Order.created]
    all_hours = np.array(all_hours)
    peak_hour = np.mode(all_hours)
    def get(self, request):
        render(request, {'mode': self.peak_hour})
        
class Yearly_Sales(View): #incomplete
    
    def get(self, request):
        years = [date.datetime.strftime("%Y") for date in Order.created]
        
        
        render(request, {'mode': peak_hour})
        
def total_sales(request):
    total = 0
    for order in Order:
        if order.paid:
            total += 1
    return render(request,{'total_sales': total})
    