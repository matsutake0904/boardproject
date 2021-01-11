from django.shortcuts import render,redirect
from django.contrib.auth.models import User
from django.contrib.auth import login, authenticate, logout
from .models import BoardModel
from django.contrib.auth.decorators import login_required
from django.views.generic import CreateView, DeleteView
from django.urls import reverse_lazy, reverse
import logging
import sys

# Create your views here.
logger = logging.getLogger(__name__)

def signupfunc(request):
    user2 = User.objects.all()
    print(user2)
    if request.method == 'POST':
        user_name = request.POST['username']
        password = request.POST['password']
        try:
            User.objects.get(username=user_name)
            return render(request, 'signup.html',{'error':'This username is already resistered !'})
        except:
            user = User.objects.create_user(user_name, ' ', password)
            login(request, user)
            return redirect('login') 
     

    ##return data conbined template 
    return render(request, 'signup.html', {'some' : 100})

def loginfunc(request):
    if request.method == 'POST':
        username2 = request.POST['username']
        password = request.POST['password']
        user = authenticate(request, username=username2, password= password)
        if user is not None:
            login(request, user)
            return redirect('list')
        else:
            return render(request,'login.html', {'error': 'This username or/and password is not registed. Please Signup!'})
    return render(request, 'login.html', {'some' : 100})

@login_required
def listfunc(request):
        object_list = BoardModel.objects.all().order_by('pk')
        return render(request, 'list.html', {'object_list' : object_list})

def logoutfunc(request):
    logout(request)
    return redirect('login')

def detailfunc(request, pk):
    object=BoardModel.objects.get(pk=pk)
    object_list = BoardModel.objects.all() 
    print('detail')
    return render(request, 'detail.html',{'object': object, 'object_list':object_list})

# def goodfunc(request, pk):
#     post = BoardModel.objects.get(pk=pk)
#     post.good = post.good + 1
#     post.save()
#     print('good')
#     return redirect('list')

def checkedfunc(request, pk):
    post = BoardModel.objects.get(pk=pk)
    if (post.checked):
        post.checked = False
    else:
        post.checked = True
    post.save()
    return redirect('list')

def checkedfunc_del(request, pk):
    post = BoardModel.objects.get(pk=pk)
    if (post.checked):
        post.checked = False
    else:
        post.checked = True
    post.save()
    object_list = BoardModel.objects.all() 
    return render(request, 'detail.html',{'object': post, 'object_list':object_list})

def readfunc(request, pk):
    post = BoardModel.objects.get(pk=pk)
    post2 = request.user.get_username()
    if post2 in post.readtext:
        return redirect('list')
    else:
        post.read += 1  
        post.readtext = post.readtext + ' ' + post2
        post.save()
        return redirect('list')      

class BoardDelete(DeleteView):
    template_name = 'delete.html'
    model = BoardModel
    success_url = reverse_lazy('list')

class BoardCreate(CreateView):
    template_name = 'create.html'
    model = BoardModel
    branch = 0
    fields = ('title', 'content', 'auther' , 'images', 'files','branch')
    # success_url = reverse_lazy('list')
    def get_success_url(self):
        if self.request.POST.get('branch') == '0':
            print('branch == ' + str(self.request.POST.get('branch')))
            return reverse('list')
        else:
            print('branch == ' + str(self.request.POST.get('branch')))
            return reverse('detail', kwargs={"pk": self.request.POST.get('branch')})
        
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        if(self.kwargs.get('pk') != None):
            context['branch']=self.kwargs.get('pk')
        else:
            context['branch']=0
        return context

# def siginup_func(request):
#     if request.method == 'POST':
#         username = request.POST['username']
#         password = request.POST['password']
#         user = User.objects.create_user(username, '', password)
#         return render(request, '', {})        
#     return render(request, '', {})
    # def get_queryset(self):
    #     branch=0
    #     try:
    #         self.kwargs.get('branch', branch)
    #         return branch
    #     except:
    #         return branch
 
# class BoardCreateBranch(CreateView):
#     template_name = 'create.html'
#     model = BoardModel
#     fields = ('title', 'content', 'auther' , 'images', 'branch')
#     success_url = reverse_lazy('list')
