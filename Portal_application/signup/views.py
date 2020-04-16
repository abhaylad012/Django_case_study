from django.shortcuts import render,redirect
from .models import dummy_table
from django.contrib import messages
from django.contrib.auth.decorators import login_required
# @login_required(login_url='/accounts/login/')
from product.models import product_details

from  django.contrib.auth.models import User, auth

from django.core.paginator import Paginator

# Create your views here.
def home(request):
    product_obj = product_details.objects.all()

    paginator =  Paginator(product_obj, 4)
    
    page = request.GET.get('page')

    # ?page =2

    product_obj = paginator.get_page(page)


    # for prod in product_obj:
    #     print("prod.prod_id", prod.prod_id)
    #     print("prod.prod_name", prod.prod_name)
    #     print("prod.prod_desc", prod.prod_desc)
    #     print("prod.prod_topic", prod.prod_topic)
    #     print("prod.prod_logos", prod.prod_logo)

    return render(request, "home.html",{'prods':product_obj})


def sign_up(request):
    return render(request, "sign_up.html")

def login(request):
    return render(request, "login.html")

def header(request):
    return render(request, "head_foot.html")


def add_user(request):
    print("hello i called after sign up")

    item = dummy_table.objects.all()
    print(item)
    for i in item:
        print(i)


    print(request.method)

    if request.method == 'POST':
        mail = request.POST.get('email')
        print(mail)

        u_id = request.POST.get('u_name')
        print(u_id)

        pwd = request.POST.get('pass')
        print(pwd)

        conf_pwd = request.POST.get('pass_conf')
        print(conf_pwd)

        if pwd != conf_pwd:
            print("password is no matching")
            messages.info(request, "Password is not matching")
            return render(request, "sign_up.html")
        elif User.objects.filter(username=u_id).exists():
            print("username is already taken")
            messages.info(request, "User Id is already taken")
            return render(request, "sign_up.html")
        elif User.objects.filter(email=mail).exists():
            print("email id is already taken")
            messages.info(request, "Email Id is already taken")
            return render(request, "sign_up.html")
        else:
            user = User.objects.create_user(username=u_id, password=pwd, email=mail)
            user.save();
            messages.info(request, "User is Successfully added please login to use Portal")
            print("user is created")
            return render(request, "login.html")

        # user = User.objects.create_user(username=u_id, password=pwd, email=mail)
        # user.save();
        #
        # print("user is created")


    return render(request, "sign_up.html")

def verify_user(request):
    print("In login verify")

    if request.method == 'POST':
        # mail = request.POST.get('email')
        # print(mail)

        u_id = request.POST.get('u_name')
        print(u_id)

        pwd = request.POST.get('pass')
        print(pwd)

        user = auth.authenticate(username = u_id, password = pwd)
        # user = auth.authenticate(email=mail, password=pwd)
        print(user)

        if user is not None:
            auth.login(request, user)
            messages.info(request, "Successfully login")
            return redirect('/nav/home')
            # return render(request, "home.html")
        else:
            messages.info(request, 'Invalid credentials')
            return render(request, "login.html")
    # return render(request, "header.html")


def logout(request):
    auth.logout(request)
    return redirect('/nav/home')