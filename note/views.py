from django.shortcuts import render
from .models import note
from .forms import NoteForm
from django.http import HttpResponseRedirect
# Create your views here.

def home(request):
    return render(request,'note/index.html',{})

def display(request):
    note_lst = note.objects.all()
    context = {
        'note_lst': note_lst
    }
    return render(request,'note/display.html',context)

def add(request):
    submitted = False
    if request.method == 'POST':
        form = NoteForm(request.POST)
        if form.is_valid():
            form.save()
        return HttpResponseRedirect("?submitted")
    
    else:
        form = NoteForm
        if submitted in request.GET:
            submitted = True
    return render(request,'note/add.html',{'form': form, 'submitted':submitted})