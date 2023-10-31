from django.shortcuts import render, redirect
from django.http import HttpResponse

from lists.models import Item, List


def home(request) -> HttpResponse:
    return render(request, "home.html")


def list(request) -> HttpResponse:
    items = Item.objects.all()
    return render(request, "list.html", {"items": items})


def new_list(request) -> HttpResponse:
    new_list = List.objects.create()
    Item.objects.create(text=request.POST["item_text"], list=new_list)
    return redirect("/lists/the-only-list-in-the-world/")
