from django.http import HttpResponseRedirect
from django.shortcuts import render
from django.contrib import messages
from .forms import ItemForm, UserForm

from . import models
from .models import Item
from .models import User
from .models import Commande

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
        else:
            messages.error(request, "Mauvais nom d'utilisateur/mot de passe.")
            return HttpResponseRedirect('/market/login')
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
    vendeur = User.objects.get(id=Items.vendeur_id.id)
    return render(request, 'market/items/item.html', {'Items': Items, 'vendeur': vendeur})

def add_item(request):
    if 'user_id' in request.session:
        user = User.objects.get(id=request.session['user_id'])
        if request.method == "POST":
            form = ItemForm(request.POST)
            if form.is_valid():
                Item = form.save(commit=False)
                Item.vendeur_id = user
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
        user = User.objects.get(id=request.session['user_id'])
        Item = iform.save(commit=False)
        Item.vendeur_id = user
        Item.save()
        return HttpResponseRedirect('/market')
    else:
        return render(request, 'market/items/add.html', {'form': iform})

def delete_item(request, id):
    if 'user_id' in request.session:
        user = User.objects.get(id=request.session['user_id'])
        Items = Item.objects.get(id=id)
        if user.id == Items.vendeur_id.id:
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
        if user.id == item.vendeur_id.id:
            if request.method == "POST":
                iform = ItemForm(request.POST, instance=item)
                if iform.is_valid():
                    Item_instance = iform.save(commit=False)
                    Item_instance.vendeur_id.id = user.id
                    Item_instance.save()
                    return HttpResponseRedirect('/market')
                else:
                    return render(request, 'market/items/update.html', {'form': iform, 'id': id})
            else:
                iform = ItemForm(instance=item)
                return render(request, 'market/items/update.html', {'form': iform, 'id': id})
        else:
            messages.error(request, "Vous n'êtes pas autorisé à accéder à cette page.")
            return HttpResponseRedirect('/market')
    else:
        return HttpResponseRedirect('/market/login')

def buy_item(request, id):
    if 'user_id' in request.session:
        user = User.objects.get(id=request.session['user_id'])
        item = Item.objects.get(id=id)
        vendeur = User.objects.get(id=item.vendeur_id.id)
        if user.id != item.vendeur_id.id:
            quantity_to_buy = int(request.POST['quantity'])
            item.quantity -= quantity_to_buy
            item.save()

            commande = Commande(item_id=item, user_id=user, vendeur_id=vendeur, quantity=quantity_to_buy, prix=(quantity_to_buy * item.price))
            commande.save()

            messages.success(request, f"Vous avez acheté {quantity_to_buy} {item.name} à un prix unitaire de {item.price} € pour un total de {quantity_to_buy * item.price} € auprès de {vendeur.name}.")
            return HttpResponseRedirect('/market')
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
        request.session['user_id'] = User.id
        request.session['user_name'] = User.name
        return HttpResponseRedirect('/market')
    else:
        return render(request, 'market/users/add.html', {'form': uform})

def delete_user(request, id):
    if 'user_id' in request.session:
        user = User.objects.get(id=request.session['user_id'])
        Users = User.objects.get(id=id)
        if user.id == Users.id:
            Users.delete()
            del request.session['user_id']
            del request.session['user_name']
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
            if request.method == "POST":
                if uform.is_valid():
                    user = uform.save(commit=False)
                    user.id = id
                    user.save()
                    request.session['user_name'] = user.name
                    return HttpResponseRedirect('/market')
                else:
                    return render(request, 'market/users/update.html', {'form': uform, 'id': id})
            else:
                uform = UserForm(instance=Users)
                return render(request, 'market/users/update.html', {'form': uform, 'id': id})
        else:
            messages.error(request, "Vous n'êtes pas autorisé à accéder à cette page.")
            return HttpResponseRedirect('/market')
    else:
        return HttpResponseRedirect('/market/login')

def commandes(request):
    if 'user_id' in request.session:
        user = User.objects.get(id=request.session['user_id'])
        Commandes = Commande.objects.filter(vendeur_id=user.id)
        item = Item.objects.all()
        return render(request, 'market/commandes/commande.html', {'Item': item, 'Commandes': Commandes})
    else:
        return HttpResponseRedirect('/market/login')

def delete_commande(request, id):
    if 'user_id' in request.session:
        user = User.objects.get(id=request.session['user_id'])
        commande = Commande.objects.get(id=id)
        if user.id == commande.vendeur_id.id:
            commande.delete()
            return render(request, 'market/commandes/delete.html')
        else:
            messages.error(request, "Vous n'êtes pas autorisé à accéder à cette page.")
            return HttpResponseRedirect('/market')
    else:
        return HttpResponseRedirect('/market/login')