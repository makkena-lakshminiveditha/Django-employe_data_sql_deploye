from django.shortcuts import render,redirect

# Create your views here.
from app.models import employe_model
from app.forms import employe_form

def details(request):
    data = employe_model.objects.all()

    return render(request,'app1/table.html',{'data':data})

def form_data(request):
    form = employe_form()
    if request.method == 'POST':
        form = employe_form(request.POST)
        if form.is_valid():
            form.save()
            return redirect('mytable')

    else:
        form = employe_form()
    return render(request,'app1/form.html',{'form':form})
