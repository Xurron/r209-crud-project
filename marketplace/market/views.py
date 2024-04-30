from django.http import HttpResponseRedirect
from django.shortcuts import render
from .forms import ItemForm, UserForm
from . import models
from .models import Item
from .models import User

def index(request):
    Items = Item.objects.all()
    return render(request, 'market/index.html', {'Items': Items})

def items(request, id):
    Items = Item.objects.get(id=id)
    return render(request, 'market/items/item.html', {'Items': Items})

def add_item(request):
    if request.method == "POST":
        form = ItemForm(request.POST)
        if form.is_valid():
            Item = form.save()
            return render(request, 'market/items/item.html', {'Item': Item})
        else:
            return render(request, 'market/items/add.html', {'form': form})
    else:
        form = ItemForm()
        return render(request, 'market/items/add.html', {'form': form})

def traitement_add_item(request):
    iform = ItemForm(request.POST)
    if iform.is_valid():
        Item = iform.save()
        return render(request, 'market/items/item.html', {'Item': Item})
    else:
        return render(request, 'market/items/add.html', {'form': iform})

def delete_item(request, id):
    Items = Item.objects.get(id=id)
    Items.delete()
    return render(request, 'market/items/delete.html')

def update_item(request, id):
    iform = ItemForm(request.POST)
    if iform.is_valid():
        Item = iform.save(commit=False)
        Item.id = id
        Item.save()
        return HttpResponseRedirect('/market')
    else:
        return render(request, 'market/items/update.html', {'form': iform, 'id': id})

def users(request, id):
    Users = User.objects.get(id=id)
    return render(request, 'market/users/user.html', {'Users': Users})

def add_user(request):
    if request.method == "POST":
        form = UserForm(request.POST)
        if form.is_valid():
            User = form.save()
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
    Users = User.objects.get(id=id)
    Users.delete()
    return render(request, 'market/users/delete.html')

def update_user(request, id):
    return render(request, 'market/users/update.html')