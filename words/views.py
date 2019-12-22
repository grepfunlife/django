from django.shortcuts import render
from .models import List


def list_list(request):
    lists = List.objects.all
    return render(request, 'words/list_list.html', {'lists': lists})
