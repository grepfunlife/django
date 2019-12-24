from django.shortcuts import render, get_object_or_404, redirect
from .models import List
from .forms import ListForm


def list_list(request):
    lists = List.objects.all
    return render(request, 'words/list_list.html', {'lists': lists})


def list_detail(request, pk):
    list = get_object_or_404(List, pk=pk)
    return render(request, 'words/list_detail.html', {'list': list})


def list_new(request):
    if request.method == "POST":
        form = ListForm(request.POST)
        if form.is_valid():
            list = form.save()
            list.save()
            return redirect('list_detail', pk=list.pk)
    else:
        form = ListForm()
    return render(request, 'words/list_edit.html', {'form': form})


def list_edit(request, pk):
    list = get_object_or_404(List, pk=pk)
    if request.method == "POST":
        form = ListForm(request.POST, instance=list)
        if form.is_valid():
            list = form.save()
            list.save()
            return redirect('list_detail', pk=list.pk)
    else:
        form = ListForm(instance=list)
    return render(request, 'words/list_edit.html', {'form': form})
