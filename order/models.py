from django.db import models
from accounts.models import User
from menu.models import Product

class Table(models.Model):
    name = models.CharField(max_length=100)
    availability = models.BooleanField(default=True)
    capacity = models.CharField(max_length=20)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    
    def __str__(self):
        return f'no-{self.name}'

class Order(models.Model):
    
    class StatusChoices(models.TextChoices):
        Canceled = "C", ("Cancelled")
        Done = "D", ("Done")
        InProgress = "I", ("IN progress")
    
    operator = models.ForeignKey(User, null = True, on_delete=models.CASCADE, related_name='orders') # staff
    customer_phone_number = models.DecimalField(null = True,decimal_places = 0, max_digits = 11)
    paid = models.BooleanField(default=False)
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)
    discount = models.IntegerField(blank=True, null=True, default=None)
    table = models.ForeignKey(Table,null = True, on_delete = models.CASCADE)
    description = models.TextField(null = True)
    status = models.CharField(choices = StatusChoices, default = StatusChoices.InProgress )
    
    
    class Meta:
        ordering = ('paid', '-updated')

    def __str__(self):
        return f'{self.operator} - {str(self.id)}'

    def get_total_price(self):
        total = sum(item.get_cost() for item in self.items.all())
        if self.discount:
            discount_price = (self.discount / 100) * total
            return int(total - discount_price)
        return total


class OrderItem(models.Model):
    order = models.ForeignKey(Order, on_delete=models.CASCADE, related_name='items')
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    price = models.IntegerField()
    quantity = models.IntegerField(default=1)

    def __str__(self):
        return str(self.id)

    def get_cost(self):
        return self.price * self.quantity


