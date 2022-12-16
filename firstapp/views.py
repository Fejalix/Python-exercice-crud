from django.shortcuts import (get_object_or_404, render,HttpResponseRedirect)
from .forms import ProductForm
# relative import of forms
from .models import Product


 # delete view for details
def delete_view(request, id):
    # dictionary for initial data with
    # field names as keys
    context ={}
 
    # fetch the object related to passed id
    obj = get_object_or_404(Product, id = id)
 
 
    if request.method =="POST":
        # delete object
        obj.delete()
        # after deleting redirect to
        # home page
        return HttpResponseRedirect("/firstapp/list/")
 
    return render(request, "firstapp/delete_view.html", context)
# update view for details
def update_view(request, id):
    # dictionary for initial data with
    # field names as keys
    context ={
        
    }
 
    # fetch the object related to passed id
    obj = get_object_or_404(Product, id = id)
 
    # pass the object as instance in form
    form = ProductForm(request.POST or None, instance=obj)
 
    # save the data from the form and
    # redirect to detail_view
    if form.is_valid():
        form.save()
        return HttpResponseRedirect("/firstapp/"+id)
 
    # add form dictionary to context
    context["form"] = form
 
    return render(request, "firstapp/update_view.html", context)

# pass id attribute from urls
def detail_view(request, id):
    # dictionary for initial data with
    # field names as keys
    context ={}
 
    # add the dictionary during initialization
    context["data"] = Product.objects.get(id = id)
         
    return render(request, "firstapp/detail_view.html", context)
 
def list_view(request):
    # dictionary for initial data with
    # field names as keys
    context ={}
 
    # add the dictionary during initialization
    context["dataset"] = Product.objects.all()
         
    return render(request, "firstapp/list_view.html", context)

def home_view(request):
    context ={}
 
    # create object of form
    form =  ProductForm(request.POST or None, request.FILES or None)
     
    # check if form data is valid
    if form.is_valid():
        # save the form data to model
        form.save()
        return HttpResponseRedirect("/firstapp/list/")
 
    context['form']= form
    return render(request, "firstapp/create_view.html", context)

# from .models import Question

def index(request):
    return render(request, 'firstapp/index.html')

# Create your views here.
