from django.shortcuts import render

# Create your views here.

ctx_groups = [
    {'group_id':1, 'group_name':'Here For You'},
    {'group_id':2, 'group_name':'Relationships'},
    {'group_id':3, 'group_name':'Abuse'}
]
x = "testing"

def home(request):
    return render(request, 'home.html')                             

def group(request):
    return render(request, 'group.html')            
    