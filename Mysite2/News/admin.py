from django.contrib import admin
from .models import berita, kategori,Customuser
# Register your models here.
admin.site.register(Customuser)

class categoriesAdmin(admin.ModelAdmin):
        list_display = ['namakategori']
        search_fields = ['namakategori']

 
admin.site.register(kategori, categoriesAdmin)

class beritaAdmin(admin.ModelAdmin):
        # listDisplay
        list_display = ['judul','isi','kategori','kategoriID','gambar','penulis','fotopenulis','status','publikasi','deskripsi']
        search_fields = ['judul','kategori_name']
        autocomplete_fields = ['kategori']


admin.site.register(berita,beritaAdmin)