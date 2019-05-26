from django.urls import path
from userapp import views
app_name='userapp'

urlpatterns =[
    path('login/',views.login , name='login'),
    path('loginlogic/',views.loginlogic , name='loginlogic'),
    path('register/',views.register, name='register'),
    path('registerlogic/',views.registerlogic , name='registerlogic'),
    path('registerok/',views.registerok , name='registerok'),
    path('ajax1/',views.ajax1,name='ajax1'),
    path('getcode/',views.getcode,name='getcode'),
    path('ajax2/',views.ajax2,name='ajax2'),
    path('ajax3/',views.ajax3,name='ajax3'),
    path('ajax4/',views.ajax4,name='ajax4'),
    path('getemail/',views.getemail,name='getemail'),
    path('delemail/',views.delemail,name='delemail'),
]