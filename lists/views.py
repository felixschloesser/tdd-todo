from django.shortcuts import render, redirect
from django.http import HttpResponse

from lists.models import Item, List


def home(request) -> HttpResponse:
    return render(request, "home.html")


def list(request, list_id) -> HttpResponse:
    our_list = List.objects.get(id=list_id)
    return render(request, "list.html", {"list": our_list})


def new_list(request) -> HttpResponse:
    our_list = List.objects.create()
    item_text = request.POST["item_text"]
    Item.objects.create(text=item_text, list=our_list)
    return redirect(f"/lists/{ our_list.id }/")


def add_item(request, list_id) -> HttpResponse:
    our_list = List.objects.get(id=list_id)
    item_text = request.POST["item_text"]
    Item.objects.create(text=item_text, list=our_list)
    return redirect(f"/lists/{ our_list.id }/")
