from django.urls import path
from .views import registrationView,loginView,resetPassword,updatePassword,productsView
urlpatterns = [
    path('register',registrationView,name='registrationView'),
    path('login',loginView ,name = 'loginView'),
    path('reset',resetPassword,name='resetPass'),
    path('update',updatePassword,name='updatepassword'),
    path('',productsView,name='productView')
]
