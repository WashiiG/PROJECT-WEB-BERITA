from django.shortcuts import render

# Create your views here.
def trending(request):
    return render(request,'menu/trending.html')

def Lifestyle(request):
    return render(request,'menu/Lifestyle.html')    

def Sports(request):
    return render(request,'menu/Sports.html')  

def Entertainment(request):
    return render(request,'menu/Entertainment.html')  

def Politik(request):
    return render(request,'menu/Politik.html')     

def Healty(request):
    return render(request,'menu/Healty.html') 