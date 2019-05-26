from django.urls import path
from orderapp import  views


app_name='orderapp'

urlpatterns=[
    path('car/',views.car,name='car'),
    path('ajax1/',views.ajax1,name='ajax1'),
    path('modify_book/',views.modify_book,name='modify_book'),
    path('delet/',views.delet,name='delet'),
    path('resume/',views.resume,name='resume'),
    path('adress/',views.adress,name='adress'),
    path('indent/',views.indent,name='indent'),
    path('ajax2/',views.ajax2,name='ajax2'),
    path('order/',views.order,name='order'),
    path('sport/',views.sport,name='sport'),
]