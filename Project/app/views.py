from django.shortcuts import render
from django.shortcuts import redirect
from django.views.decorators.csrf import csrf_exempt
from django.views.decorators.cache import cache_control
from django.contrib.auth import logout
from django.shortcuts import render_to_response
from .models import Aplication,Accept,Reject
# Create your views here.
def login(request):
    state="hiiii"

    return render(request,'home.html',{'state': state})

#LogoutHere
def pagelogout(request):
    if request.method == "POST":
        logout(request)

        return redirect('home.html')

@csrf_exempt
# @cache_control(no_cache=True, must_revalidate=True, no_store=True)
def admin_loginpage(request):
    state="login"
    print(state)
    if request.POST:
        username = request.POST.get('username')
        password = request.POST.get('password')
        # print(username,password)
        if username=="admin@email.com" and password=="test":
            application_details = Aplication.objects.all()
            accept_details = Accept.objects.all()
            reject_details = Reject.objects.all()
            # print("All objeects...!")
            # print(application_details)
            return render(request,'admin_page.html',{'application_details': application_details,'accept_details':accept_details,'reject_details':reject_details})
        else:
            return render(request,'home.html',{'state': state})

@csrf_exempt
def submit_app(request):
     state="hiiii"
     if request.POST:
        app_name = request.POST.get('app_name')
        domain_name = request.POST.get('domain_name')
        email = request.POST.get('email')
        requirement = request.POST.get('requirement')
        # print(app_name,domain_name,email,requirement)
        app = Aplication()
        app.app_name = app_name
        app.domain_name = domain_name
        app.email = email
        app.requirement = requirement
        app.save()


        return render(request,'home.html',{'state': state})

@csrf_exempt
def accept(request):
     state="hiiii"
     if request.POST:
        app_name = request.POST.get('app_name')
        domain_name = request.POST.get('domain_name')
        email = request.POST.get('email')
        requirement = request.POST.get('requirement')
        """Add to accept table"""
        app = Accept()
        app.app_name = app_name
        app.domain_name = domain_name
        app.email = email
        app.requirement = requirement
        app.save()
        """Delete form Application table"""
        instance = Aplication.objects.get(app_name=app_name,domain_name=domain_name,email=email,requirement=requirement)
        instance.delete()
        # print("inside accept")
        # print(app_name,domain_name,email,requirement)
        application_details = Aplication.objects.all()
        accept_details = Accept.objects.all()
        reject_details = Reject.objects.all()
        # print("All objeects...!")
        # print(application_details)
        return render(request,'admin_page.html',{'application_details': application_details,'accept_details':accept_details,'reject_details':reject_details})

@csrf_exempt
def reject(request):
     state="hiiii"
     if request.POST:
        app_name = request.POST.get('app_name')
        domain_name = request.POST.get('domain_name')
        email = request.POST.get('email')
        requirement = request.POST.get('requirement')
        # print("inside reject")
        # print(app_name,domain_name,email,requirement)
        """Add to Reject table"""
        app = Reject()
        app.app_name = app_name
        app.domain_name = domain_name
        app.email = email
        app.requirement = requirement
        app.save()
        """Delete form Aplication table"""
        instance = Aplication.objects.get(app_name=app_name,domain_name=domain_name,email=email,requirement=requirement)
        instance.delete()
        application_details = Aplication.objects.all()
        accept_details = Accept.objects.all()
        reject_details = Reject.objects.all()
        # print("All objeects...!")
        # print(application_details)
        return render(request,'admin_page.html',{'application_details': application_details,'accept_details':accept_details,'reject_details':reject_details})