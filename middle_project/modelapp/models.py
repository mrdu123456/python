import datetime

from django.db import models

# Create your models here.
class User(models.Model):
    username=models.CharField(max_length=40)
    email=models.CharField(max_length=40)
    password=models.CharField(max_length=128,null=True, blank=True)
    statue=models.CharField(max_length=20)
    salt=models.CharField(max_length=128,null=True, blank=True)
    create_time=models.DateTimeField(auto_now_add=True,null=True, blank=True)
    class Meta:
        db_table='t_user'
class Adress(models.Model):
    r_name=models.CharField(max_length=40)
    r_adress=models.CharField(max_length=40)
    e_number=models.CharField(max_length=40)
    tel=models.CharField(max_length=40)
    phone=models.CharField(max_length=40)
    user_id=models.ForeignKey(to=User,on_delete=models.CASCADE)
    class Meta:
        db_table='t_adress'
class Order(models.Model):
    order_id=models.CharField(max_length=40)
    create_time=models.DateTimeField(auto_now_add=True)
    all_price=models.DecimalField(max_digits=10,decimal_places=2)
    adress_id=models.ForeignKey(to=Adress,on_delete=models.CASCADE)
    user_id=models.ForeignKey(to=User,on_delete=models.CASCADE)
    statue=models.CharField(max_length=20)
    class Meta:
        db_table='t_order'

class Sort(models.Model):
    s_name=models.CharField(max_length=20)
    b_number=models.CharField(max_length=20)
    parent_id=models.IntegerField()
    level=models.IntegerField(null=True, blank=True)
    class Meta:
        db_table='t_sort'
class Book(models.Model):
    b_name=models.CharField(max_length=20, null=True, blank=True)
    author=models.CharField(max_length=40, null=True, blank=True)
    pb_house=models.CharField(max_length=80, null=True, blank=True)
    pb_time=models.DateTimeField(auto_now_add=True, null=True, blank=True)
    pb_number=models.CharField(max_length=10, null=True, blank=True)
    ibsn=models.CharField(max_length=80, null=True, blank=True)
    b_number=models.CharField(max_length=20, null=True, blank=True)
    page_number=models.CharField(max_length=20, null=True, blank=True)
    formats=models.CharField(max_length=20, null=True, blank=True)
    page=models.CharField(max_length=40, null=True, blank=True)
    pack=models.CharField(max_length=40, null=True, blank=True)
    m_price=models.DecimalField(max_digits=10,decimal_places=2, null=True, blank=True)
    d_price=models.DecimalField(max_digits=10,decimal_places=2, null=True, blank=True)
    pic=models.ImageField(upload_to='pic', null=True, blank=True)
    parent_id=models.ForeignKey(to=Sort,on_delete=models.CASCADE, null=True)
    onlinetime=models.DateTimeField(auto_now_add=True, null=True, blank=True)
    sales=models.IntegerField( null=True, blank=True)
    class Meta:
        db_table='t_book'


class Orderitem(models.Model):
    g_number=models.CharField(max_length=20)
    subtotal=models.DecimalField(max_digits=10,decimal_places=2)
    order_id=models.ForeignKey(to=Order,on_delete=models.CASCADE)
    book_id=models.ForeignKey(to=Book,on_delete=models.CASCADE)
    class Meta:
        db_table='t_orderitem'



class Confirm_string(models.Model):
    code = models.CharField(max_length=256)
    code_time = models.DateTimeField(auto_now_add=True)
    class Meta:
        db_table = 't_confirm_string'


class City(models.Model):
    cid=models.CharField(max_length=20)
    pid=models.CharField(max_length=20)
    cityname=models.CharField(max_length=255)
    types=models.CharField(max_length=20)
    class Meta:
        db_table='city'




class Code(models.Model):
    code = models.CharField(max_length=256)
    class Meta:
        db_table = 't_code'
