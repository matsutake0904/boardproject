
from django.urls import path,include
from .views import signupfunc, loginfunc, listfunc, logoutfunc, detailfunc,  BoardCreate, BoardDelete, checkedfunc, checkedfunc_del

urlpatterns = [
    path("", loginfunc, name='login'),
    path("signup/",signupfunc, name='signup'),
    path("login/", loginfunc, name='login'),
    path('list/', listfunc, name = 'list'),
    path('logout/', logoutfunc, name = 'logout'),
    path('detail/<int:pk>', detailfunc, name = 'detail'),
    path('checked/<int:pk>', checkedfunc, name = 'checked'),
    path('checked_del/<int:pk>', checkedfunc_del, name = 'checked_del'),
    # path('good/<int:pk>', goodfunc, name='good'),
    # path('read/<int:pk>', readfunc, name='read'),
    path('delete/<int:pk>', BoardDelete.as_view(), name='delete'),
    path('create/', BoardCreate.as_view(), name='create'),
    path('create/<int:pk>', BoardCreate.as_view(), name='create')

]
