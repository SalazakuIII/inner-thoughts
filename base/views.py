from django.shortcuts import render
from .models import Group
# Create your views here.



def home(request):
    groups = Group.objects.all()
    context = {'groups' : groups}
    return render(request, 'base/home.html', context)                             

def group(request, gid):
    group = Group.objects.get(id=gid)
    context = {'selected_group' : group}
    return render(request, 'base/group.html', context)           
    