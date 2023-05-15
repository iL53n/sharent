from django.shortcuts import render
from item.models import Item


def index(request):
    items = Item.objects.all()[0:8]
    return render(request, './index.html', {'items': items})
