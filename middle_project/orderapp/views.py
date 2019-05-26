from django.db import transaction
from django.shortcuts import render,HttpResponse,reverse,redirect
from django.http import JsonResponse
from modelapp.models import Book,User,Adress,Order,Orderitem,City
import uuid
# Create your views here.

class Cartitem():
    def __init__(self,book,amount,price):
        self.book=book
        self.amount=amount
        self.status=1
        self.price=price
    def sums(self):
        self.price=self.book.d_price*self.amount

class Cart():
    def __init__(self):
        self.save_price=0
        self.total_price=0
        self.cartitem=[]
        self.stus=[]
    def sums(self):
        self.total_price=0
        self.save_price=0
        for i in self.cartitem:
            if i.status==1:
                self.total_price+=i.book.d_price*i.amount
                self.save_price+=(i.book.m_price-i.book.d_price)*i.amount

    def appen(self):
        for i in self.cartitem:
            if i.status==0:
                self.stus.append(i)
    def add_book(self,book,amount):
        for i in self.cartitem:
            if i.book==book:
                i.status=1
                if i in self.stus:
                    self.stus.remove(i)
                i.amount+=amount
                i.price=i.book.d_price*i.amount
                self.sums()
                return
        self.cartitem.append(Cartitem(book,amount,book.d_price*amount))
        self.sums()
    def modify_book(self,book,amount):
        for i in self.cartitem:
            if i.book==book:
                i.amount=amount
                i.price=i.book.d_price*i.amount
        self.appen()
        self.sums()
    def del_book(self,book):
        for i in self.cartitem:
            if i.book==book:
                self.cartitem.remove(i)
            if i in self.stus:
                self.stus.remove(i)
        self.appen()
        self.sums()
    def res(self,book):
        for i in self.cartitem:
            if i.book==book:
                i.status=0
        self.appen()
        self.sums()
    def hyl(self,book):
        for i in self.cartitem:
            if i.book==book:
                self.stus.remove(i)
                i.status=1
        self.appen()
        self.sums()



def ajax1(request):
    id=request.GET.get('id')
    amount=request.GET.get('amount')
    cart = request.session.get('cart')
    book = Book.objects.filter(id=int(id))[0]
    if not cart:
        cart = Cart()
    cart.add_book(book, int(amount))
    request.session['cart'] = cart
    return HttpResponse('0')

def car(request):
    uname = request.session.get('uname')
    if not uname:
        uname = '1'
    h=request.GET.get('h')
    f=request.GET.get('f')
    id = request.GET.get('id')
    amount = request.GET.get('amount')
    cart = request.session.get('cart')
    if not cart:
        cart = Cart()
    if f=='1':
        book = Book.objects.filter(id=int(id))[0]
        cart.modify_book(book,int(amount))
    if h=='1':
        book = Book.objects.filter(id=int(id))[0]
        cart.add_book(book, 1)
    request.session['cart'] = cart
    return render(request,'orderapp/car.html',{'cart':cart,'uname':uname})

def modify_book(request):
    f=request.GET.get('f')
    request.session['f'] = f
    id = request.GET.get('id')
    request.session['id'] = id
    amount = request.GET.get('amount')
    request.session['amount'] = amount
    url=reverse('orderapp:car')+'?id='+id+'&amount='+amount+'&f='+f
    return redirect(url)


def delet(request):
    id=request.GET.get('id')
    book=Book.objects.filter(id=id)[0]
    cart=request.session.get('cart')
    cart.del_book(book)
    request.session['cart'] = cart
    def car(c):
        if isinstance(c,Cartitem):
            return {'id':c.book.id,'amount':c.amount,'status':c.status,'pic':str(c.book.pic),'d_price':str(c.book.d_price),'sprice':str(cart.save_price),'tprice':str(cart.total_price),'bprice':str(c.price)}
    return JsonResponse(list(cart.cartitem),safe=False,json_dumps_params={'default':car})



def resume(request):
    id=request.GET.get('id')
    f=request.GET.get('f')
    flag=request.GET.get('flag')
    book=Book.objects.filter(id=id)[0]
    cart=request.session.get('cart')
    if flag:
        cart.hyl(book)
    else:
        cart.res(book)
    request.session['cart']=cart
    if f:
        return redirect('orderapp:indent')
    return redirect('orderapp:car')



def adress(request):
    uname=request.session.get('uname')
    targ=request.GET.get('targ')
    if uname:
        return redirect('orderapp:indent')
    url=reverse('userapp:login')+'?targ='+targ
    return redirect(url)


def indent(request):
    uname = request.session['uname']
    cart = request.session.get('cart')
    user = User.objects.filter(username=uname)[0]
    adress = user.adress_set.filter(user_id=user.id)
    print(adress)
    return render(request, 'orderapp/indent.html', {'user': user, 'adress': adress, 'cart': cart,'uname':uname})


def ajax2(request):
    a=request.GET.get('a')
    print(a)
    u_adress=Adress.objects.filter(r_adress=a)
    def adr(adr):
        if isinstance(adr,Adress):
            return {'r_name':adr.r_name,'r_adress':adr.r_adress,'e_number':adr.e_number,'tel':adr.tel,'phone':adr.phone}
    return JsonResponse(list(u_adress),safe=False,json_dumps_params={'default':adr})


def order(request):
    old=request.POST.get('country')
    ship_man=request.POST.get('ship_man')
    d_adress=request.POST.get('d_adress')
    e_number=request.POST.get('e_number')
    phone=request.POST.get('phone')
    tel=request.POST.get('tel')
    cart=request.session.get('cart')
    uname=request.session.get('uname')
    user=User.objects.filter(username=uname)[0]
    order_id = str(uuid.uuid4())
    a=0
    if cart.total_price==0:
        return redirect('booksapp:index')
    if old:
        with transaction.atomic():
            adr=Adress.objects.filter(id=int(old))[0]
            order=adr.order_set.create(order_id=order_id,all_price=cart.total_price,statue='1',adress_id_id=adr.id,user_id_id=user.id)
            for i in cart.cartitem:
                if i.status==1:
                    a += i.amount
                    print(a)
                    cart.res(i.book)
                    Orderitem.objects.create(g_number=str(i.amount),subtotal=i.price,book_id_id=i.book.id,order_id_id=order.id)
            request.session['cart']=cart
    else:
        with transaction.atomic():
            adr=Adress.objects.create(r_name=ship_man,r_adress=d_adress,e_number=e_number,tel=tel,phone=phone,user_id_id=user.id)
            order=adr.order_set.create(order_id=order_id,all_price=cart.total_price,statue='1',adress_id_id=adr.id,user_id_id=user.id)
            for i in cart.cartitem:
                if i.status==1:
                    a+=i.amount
                    print(a)
                    cart.res(i.book)
                    Orderitem.objects.create(g_number=str(i.amount),subtotal=i.price,book_id_id=i.book.id,order_id_id=order.id)
            request.session['cart'] = cart
    return render(request,'orderapp/indent ok.html',{'order':order,'adr':adr,'uname':uname,'a':a})


def sport(request):
    id=request.GET.get('id')
    xx=City.objects.filter(pid=id)
    def china(c):
        if isinstance(c,City):
            print(c.cid)
            return {'name':c.cityname,'id':str(c.cid)}
    return JsonResponse(list(xx),safe=False,json_dumps_params={'default':china})