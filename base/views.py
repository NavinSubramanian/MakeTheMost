from django.shortcuts import render,redirect
from django.http import HttpResponse
from django.contrib.auth.forms import UserCreationForm
from .models import *
from django.contrib import messages
from django.contrib.auth.models import User
from django.contrib.auth import authenticate,login,logout
from .forms import CreateUserForm
from django.contrib.auth.decorators import login_required
from django.views.generic import CreateView

# @login_required(login_url='/login')
def home(request):
    return render(request, 'base/home.html')

def SignupPage(request):
    if request.user.is_authenticated:
        return redirect('/home')
    else:
        form = CreateUserForm()

        if request.method == 'POST':
            form = CreateUserForm(request.POST)
            if form.is_valid():
                form.save()
                messages.success(request, 'Account was created')

                return redirect('/login')

        context = {'form':form}
        return render(request, 'base/register.html',context)

def LoginPage(request):
    if request.user.is_authenticated:
        return redirect('/home')
    else:
        if request.method == 'POST':
            username = request.POST.get('username')
            password = request.POST.get('password')

            user = authenticate(request, username=username, password=password)

            if user is not None:
                login(request, user)
                return redirect('home')
            else:
                messages.info(request, 'Username or Password in wrong')

        context = {}
        return render(request, 'base/login.html', context)
 
def logoutUser(request):
    logout(request)
    return redirect('/login')

def ingridients(request):
    all_item = Items.objects.all()
    context = {'all_item':all_item}
    return render(request, 'base/ingridients.html',context)

def sepitem(request,pk):
    al = Items.objects.get(link=pk)
    waste = Waste.objects.filter(link=al)
    context = {'waste':waste}
    context['link'] = al
    return render(request, 'base/sepitem.html',context)

def seprecipe(request,pk,pl):
    al = Items.objects.filter(link=pk)
    waste = Waste.objects.get(wname=pl)
    recipe = RecipeList.objects.filter(wname=waste)
    context={'recipe':recipe,"al":al}
    return render(request, 'base/recipelist.html',context)

def search(request):
    if request.method == "POST":
        searched = request.POST['searched']
        itemss = Items.objects.filter(name__contains = searched)
        return render(request,'base/searched.html',{'searched':searched, 'itemss':itemss})
    else:
        all_item = Items.objects.all()
        return render(request,'base/ingridients.html',{'all_items':all_item})
    
def recdetail(request,pk,pl,ps):
    al = Items.objects.filter(link=pk)
    waste = Waste.objects.filter(wname=pl)
    recipe = RecipeList.objects.get(recipelink=ps)
    mainrecipe = RecipeDetail.objects.filter(recipename=recipe)

    if request.method == 'POST':
        messages = request.POST['commentt']
        print(messages)
        coment = Comment(recipename=recipe,body=messages)
        coment.save()
    
    context={'mainrecipe':mainrecipe,"al":al,"waste":waste,"recipe":recipe}
    return render(request,'base/recipedetail.html',context)

def findrecipe(request):
    recipe = RecipeList.objects.all()
    mainrecipe = RecipeDetail.objects.all()
    context = {"recipe":recipe}
    return render(request,'base/findrecipe.html',context)

# class AddCommentView(CreateView):
#     model = Comment
#     fields = '__all__'