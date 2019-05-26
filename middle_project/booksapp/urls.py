from django.urls import path
from booksapp import views

app_name='booksapp'


urlpatterns =[
    path('index/',views.index,name='index'),
    path('bookdetails/',views.bookdetails,name='bookdetails'),
    path('booklist/',views.booklist,name='booklist'),
    path('ajax1/',views.ajax1,name='ajax1'),
    path('ajax2/',views.ajax2,name='ajax2'),
    path('ajax3/',views.ajax3,name='ajax3'),
]