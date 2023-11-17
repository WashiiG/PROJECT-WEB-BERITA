from django.shortcuts import render, get_object_or_404
from. import models
# Create your views here.

def all(request):
    if 'cari' in request.GET:
        cari = request.GET['cari']
        berita = models.berita.objects.filter(judul__icontains=cari)
    else :
        berita = models.berita.objects.all()
    
    context = {'beritas' : berita}
    return render(request, 'menu/all.html', context)

def isi (request, id):
    berita = get_object_or_404(models.berita, pk=id)
    context = {'beritas' : berita}
    return render(request, 'menu/berita.html', context)


def trending (request):
   
    berita = models.berita.objects.filter(status='publish')
    kategori = models.kategori.objects.all()
    catID = 19
    if catID : 
        berita = models.berita.objects.filter(kategori = catID)
    else :
        berita = models.berita.objects.filter(status = 'publish')

    context = {'beritas' : berita, 'kategori' : kategori}

    return render(request, 'menu/trending.html', context)

def Politik (request):
    berita = models.berita.objects.filter(status='publish')
    kategori = models.kategori.objects.all()
    catID = 20
    if catID : 
        berita = models.berita.objects.filter(kategori = catID)
    else :
        berita = models.berita.objects.filter(status = 'publish')

    context = {'beritas' : berita, 'kategori' : kategori}

    return render(request, 'menu/Politik.html', context)

def Sports (request):
    berita = models.berita.objects.filter(status='publish')
    kategori = models.kategori.objects.all()
    catID = 21
    if catID : 
        berita = models.berita.objects.filter(kategori = catID)
    else :
        berita = models.berita.objects.filter(status = 'publish')

    context = {'beritas' : berita, 'kategori' : kategori}
    return render(request, 'menu/Sports.html', context)

def Lifestyle (request):
    berita = models.berita.objects.filter(status='publish')
    kategori = models.kategori.objects.all()
    catID = 4
    if catID : 
        berita = models.berita.objects.filter(kategori = catID)
    else :
        berita = models.berita.objects.filter(status = 'publish')

    context = {'beritas' : berita, 'kategori' : kategori}
    return render(request, 'menu/Lifestyle.html', context)

def Entertainment (request):
    berita = models.berita.objects.filter(status='publish')
    kategori = models.kategori.objects.all()
    catID = 23
    if catID : 
        berita = models.berita.objects.filter(kategori = catID)
    else :
        berita = models.berita.objects.filter(status = 'publish')

    context = {'beritas' : berita, 'kategori' : kategori}
    return render(request, 'menu/Entertainment.html', context)

def Healty (request):
    berita = models.berita.objects.filter(status='publish')
    kategori = models.kategori.objects.all()
    catID = 6
    if catID : 
        berita = models.berita.objects.filter(kategori = catID)
    else :
        berita = models.berita.objects.filter(status = 'publish')

    context = {'beritas' : berita, 'kategori' : kategori}
    return render(request, 'menu/Healty.html', context)