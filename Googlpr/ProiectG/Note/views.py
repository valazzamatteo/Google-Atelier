from django.shortcuts import render
from django.http import HttpResponse,HttpResponseRedirect
from django.contrib.auth.decorators import login_required
from .models import Notes
from .forms import CreateNewNota
# Create your views here.

def home(request):
    return render(request, "Note/home.html", {})

@login_required
def update(request, id):
    note = Notes.objects.get(id=id)
    if request.method == "POST":
        form = CreateNewNota(request.POST, instance=note)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect("/list")
    else:
        form = CreateNewNota(instance=note)
    return render(request, 'Note/update.html', {"form": form, "note": note})

@login_required
def delete(request, id):
    note = Notes.objects.get(id=id)
    if request.method == "POST":
        note.delete()
        return HttpResponseRedirect("/list")
    return render(request, 'Note/delete.html', {"note":note})
@login_required

def nota(request, id):
    note = Notes.objects.get(id=id)
    return render(request, 'Note/nota.html', {"note": note})
@login_required
def lista(request):
    lista = Notes.objects.filter(user=request.user).order_by('-date')
    return render(request, "Note/list.html", {"lista": lista})
@login_required
def creat(request):
    if request.method == "POST":
        form = CreateNewNota(request.POST)
        if form.is_valid():
            n = Notes(name=form.cleaned_data["name"], text=form.cleaned_data["text"])
            n.user=request.user
            n.save()
            return HttpResponseRedirect("/list")
    else:
        form = CreateNewNota()
    return render(request, 'Note/creat.html', {"form": form})
