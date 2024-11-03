from django.shortcuts import render, redirect
from . models import Checkout
from django.contrib.auth import authenticate
from .forms import Checkoutform

# menu navigations
def index(request):
    return render(request, 'index.html')
def cloth(request):
    return render(request, 'clothing.html')
def vendors(request):
    return render(request, 'vendors.html')
def contact(request):
    return render(request, 'contact.html')
def accessories(request):
    return render(request, 'accessories.html')

# Checkout view
def checkout(request):
    context = {}
    if request.POST:
        form = Checkoutform(request.POST)
        if form.is_valid():
            form.save()
            name = form.cleaned_data.get('name')
            email = form.cleaned_data.get('email')
            phone = form.cleaned_data.get('phone')
            address = form.cleaned_data.get('address')
            city    = form.cleaned_data.get('city')
            state   = form.cleaned_data.get('state')
            payment_method = form.cleaned_data.get('payment_method')
            account = authenticate(name=name,
                                   email=email,
                                   phone=phone,
                                   address=address,
                                   city=city,
                                   state=state,
                                    payment_method=payment_method,)
            # return redirect('index')
            context['success_msg'] = 'Payment Successfully!'
        else:
            context['checkout'] = form
    else:
        form = Checkoutform()
        context['checkout'] = form
    return render(request, 'checkout.html', context)


# Feature products
def womenG(request):
    return render(request, 'featurepro/womenG.html')
def womenG2(request):
    return render(request, 'featurepro/womenG2.html')

def silver1(request):
    return render(request, 'featurepro/silver1.html')
def silver2(request):
    return render(request, 'featurepro/silver2.html')

def officeL(request):
    return render(request, 'featurepro/officeL.html')
def officeL2(request):
    return render(request, 'featureproofficeL2.html')

# Our vendors
def g1(request):
    return render(request, 'vendors/g1.html'),
def chic(request):
    return render(request, 'vendors/chicA.html')
def urban(request):
    return render(request, 'vendors/urbanO.html'),

# Dashboard views
def dashboardview(request):
    return render(request, 'account/dashboard.html')

# def orderview(request):
#     return render(request, 'account/orders.html')