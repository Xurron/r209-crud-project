from django.http import HttpResponseRedirect
from django.shortcuts import render
from .forms import ItemForm
from . import models
from .models import Item

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

def users(request):
    return render(request, 'market/users/user.html')

def add_user(request):
    return render(request, 'market/users/add.html')

def delete_user(request, id):
    return render(request, 'market/users/delete.html')

def update_user(request, id):
    return render(request, 'market/users/update.html')