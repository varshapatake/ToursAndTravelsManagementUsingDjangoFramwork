from django.shortcuts import render
import re
from .models import Customer,AdminInfo,RegisterPackageInfo,PackageCosts,Shedule



def index(request):
    cost = PackageCosts.objects.all()
    for price in cost:
        if price.packagename == "shimala":
            shimala_cost=price.cost

        if price.packagename == "paris":
            paris_cost = price.cost
        if price.packagename == "rome":
            rome_cost = price.cost
        if price.packagename == "london":
            london_cost = price.cost
        if price.packagename == "dubai":
            dubai_cost = price.cost
        if price.packagename == "newyark":
            newyork_cost = price.cost
        if price.packagename == "hongkong":
            hongkong_cost = price.cost
        if price.packagename == "bali":
            bali_cost = price.cost
    context={"shimala_cost":shimala_cost,"paris_cost":paris_cost,"rome_cost":rome_cost,"london_cost":london_cost,"dubai_cost":dubai_cost,"newyork_cost":newyork_cost,"hongkong_cost":hongkong_cost,"bali_cost":bali_cost}
    return render(request,'tour\index.html',context)



def register(request):
    return render(request, "tour/register.html")

def login(request):
    return render(request, "tour/login.html")

def add_register_customer_submit(request):
    print ('hello form is submitted')
    name=request.POST.get("nm",'')
    age=request.POST.get("age")
    mobile=request.POST.get("mob",'')
    email=request.POST.get("email",'')
    address=request.POST.get("add",'')
    username=request.POST.get("user",'')
    password=request.POST.get("pass",'')

    if(re.search(r'(^[0-9])',name)):

        name1="error"
    else:
        name1="noerror"

    count = 0
    num=int(mobile)
    while ( num!=0):
        num = num //10
        count = count + 1

    if(count!=10):
        mobile1 = "error"
    else:
        mobile1="noerror"

    if re.search(r'(^[a-zA-Z0-9]+.+@[a-zA-Z]+\.[a-zA-Z]{1,3}$)',email):
        email1="noerror"
    else:
        email1 = "error"

    context={"mobile1":mobile1,"email1":email1,"name1":name1}
    if(mobile1=="error" or email1=="error" or name1=="error"):
        return render(request,"tour/validate_registration_form.html",context)

    customer = Customer(name=name, age=age, mobile=mobile, email=email, address=address, username=username,
                        password=password)
    customer.save()
    return render(request, 'tour/login.html')


def book_package_shimala(request):
    return render(request,"tour/shimala.html")

def book_package_paris(request):
    return render(request,"tour/paris.html")

def book_package_rome(request):
    return render(request,"tour/rome.html")

def book_package_london(request):
    return render(request,"tour/london.html")

def book_package_dubai(request):
    return render(request,"tour/dubai.html")

def book_package_new_york(request):
    return render(request,"tour/new_york.html")

def book_package_hong_kong(request):
    return render(request,"tour/hong_kong.html")

def book_package_bali(request):
    return render(request,"tour/bali.html")

def admin_login(request):
    return render(request,"tour/login.html")

def admin(request):
    return render(request,"http://127.0.0.1:8000/admin")

def login_check(request):
    username = request.POST.get("user", "")
    password = request.POST.get("pass", "")
    admin =AdminInfo.objects.get(pk=1)
    customers = Customer.objects.all()
    context={"user_name":username,"password":password,"admin":admin,"all_customers": customers}

    if (username == admin.username and password == admin.password):
        return render(request, "tour/admin.html", context)
    else:
        for customer in customers:
            if (username == customer.username and password == customer.password):
                if request.method == 'POST':
                    request.session['username'] = username

                return render(request, "tour/customer_package_view.html",{"username":username})
        else:
            return render(request,"tour/invalidlogin.html")

def about_us(request):
    return render(request,"tour/about_us.html")

def help(request):
    return render(request,"tour/help.html")

def logout_check(request):
    return render(request, "tour/login.html")

def places(request):
    return render(request, "tour/index.html")

def register_package(request):
    if request.session.has_key('username'):
        username = request.session['username']
    return render(request,"tour/register_package.html",{"username":username})


def submit_register_packageinfo(request):
    if request.session.has_key('username'):
        username = request.session['username']
    name = request.POST.get("nm",'')
    gender=request.POST.get("gender",'')
    age = request.POST.get("age")
    mobile = request.POST.get("mob",'')
    email = request.POST.get("email",'')
    package_name=request.POST.get("package",'')
    if request.method == 'POST':
        request.session['package_name'] =package_name

    context={"name":name,"gender":gender,"age":age,"mobile":mobile,"email":email,"package_name":package_name,"username":username}
    reg=RegisterPackageInfo.objects.all()

    if reg:
        for register in reg:
            if register.email== email:
                return render(request,"tour/user_already_exists_with_email.html")
            else:
                register = RegisterPackageInfo(name=name, gender=gender, age=age, mobile=mobile, email=email,
                                               package_name=package_name,user_name=username)
                register.save()
                return render(request,"tour/validate_user_info.html",context)

def calculate_package_cost(request):
    if request.session.has_key('package_name'):
        package_name = request.session['package_name']
    cost=PackageCosts.objects.all()
    for price in cost:
         if price.packagename==package_name:
             context={"package_cost":price.cost}
    return render(request,"tour/payment_options.html",context)

def customer_package_view(request):
    return render(request,"tour/customer_package_view.html")

def submit_payment(request):
    name = request.POST.get("nm", "")
    email = request.POST.get("mail", "")
    card_no = request.POST.get("card")
    amount = request.POST.get("amt")
    context = { "name": name, "email": email, "card_no":card_no, "amount":amount}
    return render(request,"tour/payment_successful.html",context)


def registration_successfull(request):
    return render(request,"tour/package_registration_successful.html")


def register_count(request):
    if request.session.has_key('username'):
        username = request.session['username']
    register_user=RegisterPackageInfo.objects.all()
    context={"username":username,"register_user":register_user}
    return render(request,"tour/show_register_user_from_account.html",context)

def profile(request):
    if request.session.has_key('username'):
        username = request.session['username']
    customer=Customer.objects.all()
    context={"username":username,"customer":customer}
    return render(request,"tour/profile.html",context)


def shedule(request):
    if request.session.has_key('username'):
        username = request.session['username']
    register_user = RegisterPackageInfo.objects.all()
    shedule=Shedule.objects.all()
    context={"username":username,"register_user":register_user,"shedule":shedule}
    return render(request,"tour/shedule.html",context)




