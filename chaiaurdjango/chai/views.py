from django.shortcuts import render
from .models import ChaiVariety,Stores
from .forms import ChaiVarietyForm

# Create your views here.
def all_chai(request):
    chais=ChaiVariety.objects.all()
    return render(request,'all_chai.html',{'chais':chais})

def chai_store_view(request):
    stores=None
    if request.method=='POST':
        form=ChaiVarietyForm(request.POST)
        if form.is_valid():
            chai_varity=form.cleaned_data['chai_variety']
            Stores.objects.filter(chai_varities=chai_varity)
    else:
        form=ChaiVarietyForm()
    return render(request,'chai_stores.html',{'stores':stores, 'form':form})

