from django.shortcuts import render
from movieapp.models import Movie
from movieapp.forms import Movieform
# Create your views here.
def home(request):
    h = Movie.objects.all()
    return render(request, 'home.html', {'m': h})
def addmovie(request):
    if (request.method == "POST"):
        n = request.POST['n']
        d = request.POST['d']
        y = request.POST['y']
        i = request.FILES['i']
        m = Movie.objects.create(name=n, description=d, year=y, image=i)
        m.save()
        return home(request)
    return render(request, 'addmovie.html')
def moviedetails(request,p):
    m = Movie.objects.get(id=p)
    return render(request, 'moviedetails.html', {'m': m})
def deletemovie(request,p):
    m=Movie.objects.get(id=p)
    m.delete()
    return home(request)
def updatemovie(request,p):
    m=Movie.objects.get(id=p)
    if (request.method == "POST"):
        form = Movieform(request.POST,request.FILES,instance=m)
        if form.is_valid():
            form.save()
        return home(request)
    form=Movieform(instance=m)
    return render(request, 'update.html', {'form': form})