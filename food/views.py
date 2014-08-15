# Create your views here.
from django.contrib import auth
from django.http import HttpResponseRedirect, HttpResponse
from django.contrib.auth.forms import UserCreationForm
from django.shortcuts import render, render_to_response
from django.contrib.auth.decorators import login_required
from food.forms import ProductForm, SearchForm
from food.models import Product
from django.template.context import RequestContext
from django.utils import simplejson

def logout_view(request):
    auth.logout(request)
    # Redirect to a success page.
    return HttpResponseRedirect("/account/loggedout/")

def register(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            new_user = form.save()
            return HttpResponseRedirect("/accounts/login/")
    else:
        form = UserCreationForm()
    return render(request, "registration/register.html", {
        'form': form,
    })

@login_required
def add_product(request):
    print "add_product"
    if request.method == 'POST':
        print 'inside post'
        form = ProductForm(request.POST)
        if form.is_valid():
            print "form valid"
            product_name = form.cleaned_data['product_name']
            product_description  = form.cleaned_data['product_description']
            print product_name
            print product_description
            product = Product.objects.create(
                                             name = product_name,
                                             description = product_description)
            product.save()
            print product.name
            return HttpResponseRedirect('/accounts/profile')
        else:
            form = ProductForm()
        return render_to_response('add_product.html', locals(), context_instance=RequestContext(request))
    else:
        form = ProductForm()
    return render_to_response('add_product.html', locals(), context_instance=RequestContext(request))
    
@login_required
def profile(request):
    print "profile"
    products = Product.objects.all()
    print products
    return render_to_response('profile.html', locals(), context_instance=RequestContext(request))

@login_required
def search_product_autocomplete(request):
    product_data = []
    if request.GET.has_key(u'term'):
        value = request.GET[u'term']
        if len(value) > 1:
            try:
                products = Product.objects.all()
                for product in products:
                    product_data.append(dict([('label', product.name), ('value', product.name)]))
            except Exception as e:
                print e
    json = simplejson.dumps([product for product in product_data])
    return HttpResponse(json, mimetype = 'application/json')

@login_required
def search_product(request):
    print "search prod"
    if request.method == "POST":
        form = SearchForm(request.POST)
        if form.is_valid():
            try:
                product = Product.objects.get(name = form.cleaned_data['search'])
                product_name = product.name
                product_id = product.id
                return HttpResponseRedirect("/accounts/product/view/"+str(product_id))
            except Exception as e:
                error = "The product doesnot exist"
                return render_to_response('view_product.html',locals(), context_instance=RequestContext(request))
        else:
            form = SearchForm()
            return render_to_response('profile.html',locals(), context_instance=RequestContext(request))
    else:
        form = SearchForm()
        return render_to_response('profile.html',locals(), context_instance=RequestContext(request))

@login_required
def view_product(request,product_id):
    print "view product"
    product = Product.objects.get(id = product_id)
    return render_to_response('view_product.html', locals(), context_instance=RequestContext(request))
