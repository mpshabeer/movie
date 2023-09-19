from django.http import HttpResponse
from django.shortcuts import render, redirect

from .forms import movieform
from movieapp .models import movie
# Create your views here.
def index(request):
    movies=movie.objects.all()

    c={
        'movielist':movies
    }
    return render(request,"index.html",c)


def moviedetail(request,movie_id):
    m=movie.objects.get(id=movie_id)
    return render(request,"details.html",{'movie':m})

def upload(request):
    if request.method=='POST':
        name=request.POST['name']
        desc=request.POST['desc']
        year=request.POST['year']
        imgs=request.FILES['img']
        m=movie()
        m.name=name
        m.desc=desc
        m.year=year
        m.img=imgs
        m.save()
        return redirect('/')


    return render(request,'upload.html')

def update(request,id):
    movies=movie.objects.get(id=id)
    form=movieform(request.POST or None,request.FILES,instance=movies)
    if form.is_valid():
        form.save()
        return redirect('/')
    return render(request,"edit.html",{'form':form,'movie':movies})

def delete(request,id):
    if request.method=='POST':
        movies=movie.objects.get(id=id)
        movies.delete()
        return redirect('/')
    return render(request,"delete.html")
