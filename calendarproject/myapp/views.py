from django.shortcuts import render,get_object_or_404
from django.http import HttpResponseRedirect
from .models import Entry
from .forms import EntryForm

# Create your views here.
def index(request):
    #return HttpResponse('<h1>It Works!</h1>')
    entries=Entry.objects.all()
    return render(request,'myapp/index.html',{'entries':entries})
def details(request,pk):
    entry=get_object_or_404(Entry,pk=pk)
    return render(request,'myapp/details.html',{'entry':entry})
def add(request):
    if request.method=="POST":
        form=EntryForm(request.POST)
        if form.is_valid():
            name=form.cleaned_data['name']
            date=form.cleaned_data['date']
            description=form.cleaned_data['description']
            Entry.objects.create(
              name=name,
              date=date,
              description=description,
            ).save()
            return HttpResponseRedirect('/')
    else:
        form=EntryForm()
    return render(request,'myapp/form.html',{'form':form})
