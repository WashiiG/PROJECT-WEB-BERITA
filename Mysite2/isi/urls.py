from django.urls import path
from. import views

app_name = 'isi'

urlpatterns = [
    path('berita/',views.isi,name ='berita.html')
]