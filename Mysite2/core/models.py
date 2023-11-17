from django.db import models
from News import models as mdl
# Create your models here.
class beritaupdate1(models.Model):
    STATUS = ('publish', 'publish'),('draft', 'draft')

    judul = models.CharField(max_length=255)
    isi = models.CharField(max_length=9999)
    kategori = models.ForeignKey(mdl.kategori,on_delete=models.CASCADE)
    kategoriID = models.IntegerField()
    gambar = models.ImageField(upload_to='media', height_field=None, width_field=None, max_length=100)
    penulis = models.CharField(max_length=255)
    fotopenulis = models.ImageField(upload_to='media', height_field=None, width_field=None, max_length=100, null=True)
    status = models.CharField(choices=STATUS, max_length=200)
    publikasi = models.CharField(max_length=255)    
    deskripsi = models.CharField(max_length=255)