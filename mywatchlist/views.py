from django.shortcuts import render
from mywatchlist.models import MyWatchlist
from django.http import HttpResponse
from django.core import serializers

# Create your views here.
def show_watchlist(request):
    data_watchlist = MyWatchlist.objects.all()
    is_watched = 0
    not_watched = 0
    for a in data_watchlist:
        if a.watched:
            is_watched += 1
        else:
            not_watched += 1
    context = { 
        'list_item': data_watchlist,
        'nama': 'Vladi Jingga Mentari',
        'student_id': '2106635631',
        'x': is_watched,
        'y': not_watched,
    }
    return render(request, "mywatchlist.html", context)

def show_xml(request):
    data = MyWatchlist.objects.all()
    return HttpResponse(serializers.serialize("xml", data), content_type="application/xml")

def show_json(request):
    data = MyWatchlist.objects.all()
    return HttpResponse(serializers.serialize("json", data), content_type="application/json")

def show_xml_by_id(request,id):
    data = MyWatchlist.objects.all()
    return HttpResponse(serializers.serialize("xml", data), content_type="application/xml")

def show_json_by_id(request, id):
    data = MyWatchlist.objects.all()
    return HttpResponse(serializers.serialize("json", data), content_type="application/json")