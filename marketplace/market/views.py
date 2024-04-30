from django.shortcuts import render

def index(request):
    return render(request, 'market/index.html')

def items(request):
    return render(request, 'market/items/item.html')

def add_item(request):
    return render(request, 'market/items/add.html')

def delete_item(request, id):
    return render(request, 'market/items/delete.html')

def update_item(request, id):
    return render(request, 'market/items/update.html')

def users(request):
    return render(request, 'market/users/user.html')

def add_user(request):
    return render(request, 'market/users/add.html')

def delete_user(request, id):
    return render(request, 'market/users/delete.html')

def update_user(request, id):
    return render(request, 'market/users/update.html')