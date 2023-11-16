from django.shortcuts import render
from News import models as mdl
# Create your views here.

def isi(request, pk):
    berita = mdl.berita.objects.get(pk=pk)
    context = {'beritas' : berita}
    return render(request, 'berita/berita.html', context)