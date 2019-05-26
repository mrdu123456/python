from django.shortcuts import render, redirect,reverse,HttpResponse
from modelapp.models import Sort,Book,User
from django.core.paginator import Paginator
import  time
# Create your views here.
def index(request):
    uname = request.session.get('uname')
    name = request.COOKIES.get('name')
    if name:
        name = request.COOKIES.get('name')
        password = request.COOKIES.get('password')
        res = User.objects.filter(username=name, password=password)
        if res:
            request.session['uname'] = name
            uname=name
    uname=request.session.get('uname')
    if not uname:
        uname='1'
    print(uname,'index')
    st=Sort.objects.filter(parent_id__in=(0,100,101,102,103,104,105,106,107,108))
    st2=Sort.objects.filter(parent_id__gt=0)
    st3=Sort.objects.filter(parent_id=103)
    books=Book.objects.all().order_by('pb_time')[0:8]
    author=Book.objects.all().order_by('author')[0:8]
    bo=Book.objects.all().order_by('sales')[0:5]
    return render(request,'booksapp/index.html',{'st':st,'st2':st2,'st3':st3,'books':books,'author':author,'bo':bo,'uname':uname})
def bookdetails(request):
    uname=request.session.get('uname')
    if not uname:
        uname='1'
    bookid=request.GET.get('bookid')
    book=Book.objects.filter(id=int(bookid))[0]
    pbtime=book.pb_time
    online=book.onlinetime
    s2=book.parent_id
    s1=Sort.objects.filter(id=s2.parent_id)[0]
    return render(request,'booksapp/Book details.html',{'book':book,'s2':s2,'s1':s1,'pbtime':pbtime,'online':online,'uname':uname})


def booklist(request):
    uname = request.session.get('uname')
    if not uname:
        uname = '1'
    f=request.GET.get('f')
    if not  f:
        f='5'
    print(f)
    number=request.GET.get('number')
    s1=request.GET.get('s1')
    s2=request.GET.get('s2')
    print(s2)
    st = Sort.objects.filter(parent_id__in=(0, 100, 101, 102, 103, 104, 105, 106, 107, 108))
    st2 = Sort.objects.filter(parent_id__gt=0)
    st3 = Sort.objects.filter(parent_id=103)
    if not number:
        number = 1
    if s2 !=None and s2 != 'None':
        s=Sort.objects.filter(id=int(s2))[0]
        print(s)
        name=Sort.objects.filter(id=int(s2))[0]
        name1 = Sort.objects.filter(id=name.parent_id)[0]
        if f=='2':
            book=s.book_set.all().order_by('-sales')
        elif f=='3':
            book=s.book_set.all().order_by('d_price')
        elif f=='4':
            book=s.book_set.all().order_by('-pb_time')
        else:
            book=s.book_set.all()
            print(book)
        pator=Paginator(book,3)
        page=pator.page(number=int(number))
    else:
        s=Sort.objects.filter(parent_id=int(s1))
        name=Sort.objects.filter(id=int(s1))[0]
        name1=[]
        l=[]
        for i in s:
            l.append(i.id)
        l=tuple(l )
        if f=='2':
            book=Book.objects.filter(parent_id__in=l).order_by('-sales')
        elif f=='3':
            book = Book.objects.filter(parent_id__in=l).order_by('d_price')
        elif f=='4':
            book = Book.objects.filter(parent_id__in=l).order_by('-pb_time')
        else:
            book = Book.objects.filter(parent_id__in=l)
        pator = Paginator(book, 3)
        page = pator.page(number=int(number))
    return render(request, 'booksapp/booklist.html', {'page': page,'st':st,'st2':st2,'st3':st3,'s1':s1,'s2':s2,'name':name,'name1':name1,'number':number,'f':f,'uname':uname})

def ajax1(request):
    number=request.GET.get('number')
    s1=request.GET.get('s1')
    s2=request.GET.get('s2')
    url=reverse('booksapp:booklist')+'?number='+number+'&s1='+s1+'&s2='+s2
    return  redirect(url)


def ajax2(request):
    number=request.GET.get('number')
    s1=request.GET.get('s1')
    s2=request.GET.get('s2')
    f=request.GET.get('f')
    url=reverse('booksapp:booklist')+'?number='+number+'&s1='+s1+'&s2='+s2+'&f='+f
    return redirect(url)



def ajax3(request):
    del request.session['uname']
    del request.session['flag']
    del request.session['targ']
    return HttpResponse('1')

