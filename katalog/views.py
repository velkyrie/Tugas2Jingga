from django.shortcuts import render
from katalog.models import CatalogItem

# TODO: Create your views here.

def show_katalog(request):
    data_barang_katalog = CatalogItem.objects.all()
    context = { 
        'list_item': data_barang_katalog,
        'nama': 'Vladi Jingga Mentari',
        'student_id': '2106635631'
    }
    return render(request, "katalog.html", context)
