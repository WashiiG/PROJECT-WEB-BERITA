from django.urls import path
from. import views

app_name = 'News'

urlpatterns = [
    path('trending/',views.trending, name ='trending'),
    path('Lifestyle/',views.Lifestyle, name ='Lifestyle'),
    path('Sports/',views.Sports, name ='Sports'),
    path('Entertainment/',views.Entertainment, name ='Entertainment'),
    path('Politik/',views.Politik, name ='Politik'),
    path('Healty/',views.Healty, name ='Healty'),
    path('all/',views.all, name ='all'),
    path('isi/<int:id>',views.isi, name ='isi'),
]