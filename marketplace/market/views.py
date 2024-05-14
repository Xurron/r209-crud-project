from django.http import HttpResponseRedirect
from django.shortcuts import render
from django.contrib import messages
from .forms import ItemForm, UserForm

from . import models
from .models import Item
from .models import User

def index(request):
    if 'user_id' in request.session:
        Items = Item.objects.all()
        return render(request, 'market/index.html', {'Items': Items})
    else:
        return HttpResponseRedirect('/market/login')

def login(request):
    if 'user_id' in request.session:
        return HttpResponseRedirect('/market')
    else:
        return render(request, 'market/login/login.html')

def login_user(request):
    if request.method == "POST":
        username = request.POST['username']
        password = request.POST['password']
        Users = User.objects.all()
        for user in Users:
            if user.verify(username, password):
                request.session['user_id'] = user.id
                request.session['user_name'] = user.name
                return HttpResponseRedirect('/market')
        return render(request, 'market/login/login.html', {'error': 'Invalid credentials'})
    else:
        return render(request, 'market/login/login.html')

def logout(request):
    if 'user_id' in request.session:
        del request.session['user_id']
        del request.session['user_name']
        return HttpResponseRedirect('/market')
    else:
        return HttpResponseRedirect('/market/login')

def items(request, id):
    Items = Item.objects.get(id=id)
    return render(request, 'market/items/item.html', {'Items': Items})

def add_item(request):
    if 'user_id' in request.session:
        user = User.objects.get(id=request.session['user_id'])
        if request.method == "POST":
            form = ItemForm(request.POST)
            if form.is_valid():
                Item = form.save(commit=False)
                Item.vendeur_id = user.id
                Item.save()
                return render(request, 'market/items/item.html', {'Item': Item})
            else:
                return render(request, 'market/items/add.html', {'form': form})
        else:
            form = ItemForm()
            return render(request, 'market/items/add.html', {'form': form})
    else:
        return HttpResponseRedirect('/market/login')

def traitement_add_item(request):
    iform = ItemForm(request.POST)
    if iform.is_valid():
        Item = iform.save(commit=False)
        Item.vendeur_id = request.session['user_id']
        Item.save()
        return render(request, 'market/items/item.html', {'Item': Item})
    else:
        return render(request, 'market/items/add.html', {'form': iform})

def delete_item(request, id):
    if 'user_id' in request.session:
        user = User.objects.get(id=request.session['user_id'])
        Items = Item.objects.get(id=id)
        if user.id == Items.vendeur_id:
            Items.delete()
            return render(request, 'market/items/delete.html')
        else:
            messages.error(request, "Vous n'êtes pas autorisé à accéder à cette page.")
            return HttpResponseRedirect('/market')
    else:
        return HttpResponseRedirect('/market/login')

def update_item(request, id):
    if 'user_id' in request.session:
        user = User.objects.get(id=request.session['user_id'])
        item = Item.objects.get(id=id)
        if user.id == item.vendeur_id:
            iform = ItemForm(request.POST)
            if iform.is_valid():
                Item_instance = iform.save(commit=False)
                Item.id = id
                Item.save()
                return HttpResponseRedirect('/market')
            else:
                return render(request, 'market/items/update.html', {'form': iform, 'id': id})
        else:
            messages.error(request, "Vous n'êtes pas autorisé à accéder à cette page.")
            return HttpResponseRedirect('/market')
    else:
        return HttpResponseRedirect('/market/login')

def users(request, id):
    if 'user_id' in request.session:
        user = User.objects.get(id=request.session['user_id'])
        Users = User.objects.get(id=id)
        if user.id == Users.id:
            return render(request, 'market/users/user.html', {'Users': Users})
        else:
            messages.error(request, "Vous n'êtes pas autorisé à accéder à cette page.")
            return HttpResponseRedirect('/market')
    else:
        return HttpResponseRedirect('/market/login')

def add_user(request):
    if 'user_id' in request.session:
        return HttpResponseRedirect('/market/login')
    else:
        if request.method == "POST":
            form = UserForm(request.POST)
            if form.is_valid():
                user = form.save()
                return render(request, 'market/users/user.html', {'User': User})
            else:
                return render(request, 'market/users/add.html', {'form': form})
        else:
            form = UserForm()
            return render(request, 'market/users/add.html', {'form': form})

def traitement_add_user(request):
    uform = UserForm(request.POST)
    if uform.is_valid():
        User = uform.save()
        return render(request, 'market/users/user.html', {'User': User})
    else:
        return render(request, 'market/users/add.html', {'form': uform})

def delete_user(request, id):
    if 'user_id' in request.session:
        user = User.objects.get(id=request.session['user_id'])
        Users = User.objects.get(id=id)
        if user.id == Users.id:
            Users.delete()
            return render(request, 'market/users/delete.html')
        else:
            messages.error(request, "Vous n'êtes pas autorisé à accéder à cette page.")
            return HttpResponseRedirect('/market')
    else:
        return HttpResponseRedirect('/market/login')

def update_user(request, id):
    if 'user_id' in request.session:
        user = User.objects.get(id=request.session['user_id'])
        Users = User.objects.get(id=id)
        uform = UserForm(request.POST)
        if user.id == Users.id:
            if uform.is_valid():
                user = uform.save(commit=False)
                user.id = id
                user.save()
                return HttpResponseRedirect('/market')
            else:
                return render(request, 'market/users/update.html', {'form': uform, 'id': id})
        else:
            messages.error(request, "Vous n'êtes pas autorisé à accéder à cette page.")
            return HttpResponseRedirect('/market')
    else:
        return HttpResponseRedirect('/market/login')