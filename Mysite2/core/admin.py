from django.contrib import admin
from . models import beritaupdate1

# Register your models here
class beritaupdate1Admin (admin.ModelAdmin):
    # List Display
    list_display = ['judul', 'deskripsi', 'isi', 'kategori', 'kategoriID', 'gambar', 'penulis', 'fotopenulis', 'publikasi', 'status']
    search_fields = ['judul', 'kategori_name']
    autocomplete_fields = ['kategori']

admin.site.register(beritaupdate1, beritaupdate1Admin)