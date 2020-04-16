from django.shortcuts import render, redirect
from .models import product_details
from django.contrib import messages
from django.conf import settings
from django.conf.urls.static import static
from django.core.files.storage import FileSystemStorage
import os

from django.core.paginator import Paginator

from django.contrib.auth.decorators import login_required


# Create your views here.
@login_required(login_url='/nav/login')
def product_form(request):
    if request.method == 'POST':
        p_name = request.POST.get('p_name')
        print(p_name)

        p_short = request.POST.get('p_short')
        print(p_short)

        p_desc = request.POST.get('p_desc')
        print(p_desc)

        p_topic = request.POST.get('p_topic')
        print(p_topic)

        p_logo = request.FILES['p_logo'] if 'p_logo' in request.FILES else False
        # p_logo = request.POST.get('p_logo')
        print(p_logo)

        prod_cr_by = request.user
        print('prod_cr_by', prod_cr_by)

        if p_logo == False:
            product = product_details(prod_name=p_name, prod_short=p_short, prod_desc=p_desc, prod_topic=p_topic,
                                  prod_logo=p_logo, prod_cr_by=prod_cr_by)
            product.save();
        else:
            product = product_details(prod_name=p_name, prod_short=p_short, prod_desc=p_desc, prod_topic=p_topic, prod_cr_by=prod_cr_by, prod_logo=p_logo)
            product.save();
        product_obj = product_details.objects.all()

        for prod in product_obj:
            print("prod.prod_id", prod.prod_id)
            print("prod.prod_name", prod.prod_name)
            print("prod.prod_desc", prod.prod_desc)
            print("prod.prod_topic", prod.prod_topic)
            print("prod.prod_logos", prod.prod_logo)

        print(product_obj[0])
        # return render(request, "home.html")
        return redirect('/nav/home')

    return render(request, "product_form.html")


def product_view(request, prod_id):
    prod = product_details.objects.get(pk=prod_id)
    print('prod', prod)
    print('prod.prod_id', prod.prod_id)
    print('prod.prod_desc', prod.prod_desc)
    # for prod_item in prod:
    #     print("prod_item.prod_id", prod.prod_id)
    #     print("prod_item.prod_name", prod.prod_name)
    #     print("prod_item.prod_desc", prod.prod_desc)
    #     print("prod_item.prod_topic", prod.prod_topic)
    #     print("prod_item.prod_logos", prod.prod_logo)
    return render(request, 'product_view.html', {'prod_id': prod.prod_id, 'prod_name': prod.prod_name,
                                                 'prod_short': prod.prod_short, 'prod_desc': prod.prod_desc,
                                                 'prod_topic': prod.prod_topic, 'prod_logo': prod.prod_logo,
                                                 'prod_cr_by': prod.prod_cr_by})

@login_required(login_url='/nav/login')
def product_delete(request, prod_id):
    prod = product_details.objects.get(pk=prod_id)
    prod.delete()
    messages.info(request, "Product : " + prod_id + " Succesfully Deleted")
    return redirect('/nav/home')

@login_required(login_url='/nav/login')
def product_edit_form(request, prod_id):
    prod = product_details.objects.get(pk=prod_id)
    return render(request, 'product_update.html', {'prod_id': prod.prod_id, 'prod_name': prod.prod_name,
                                                   'prod_short': prod.prod_short, 'prod_desc': prod.prod_desc,
                                                   'prod_topic': prod.prod_topic, 'prod_logo': prod.prod_logo})


def product_update(request, prod_id):
    p_name = request.POST.get('p_name')
    print(p_name)

    p_short = request.POST.get('p_short')
    print(p_short)

    p_desc = request.POST.get('p_desc')
    print(p_desc)

    p_topic = request.POST.get('p_topic')
    print(p_topic)

    p_logo = request.FILES['p_logo'] if 'p_logo' in request.FILES else False
    # p_logo = request.POST.get('p_logo')
    print("p_logo", p_logo)

    if p_logo is False:

        prod = product_details.objects.get(pk=prod_id)
        # prod.prod_logo =p_logo
        # prod.save();

        product_details.objects.filter(pk=prod_id).update(prod_name=p_name, prod_short=p_short, prod_desc=p_desc, prod_topic=p_topic)
    else:
        print("In else")
        prod = product_details.objects.get(pk=prod_id)
        # prod.prod_logo =p_logo
        prod.prod_logo = p_logo
        prod.save();
        print("after save")
        product_details.objects.filter(pk=prod_id).update(prod_name=p_name, prod_short=p_short, prod_desc=p_desc,
                                                          prod_topic=p_topic)
        print("after update")

    messages.info(request, "Product : " + prod_id + " Succesfully Updated")
    return redirect('/nav/home')
