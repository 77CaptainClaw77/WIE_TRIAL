#from django.shortcuts import render

# Create your views here.
#I have created this file- Prabhu T P
from wieHack.models import participants,domains

from django.shortcuts import render

from django.http import HttpResponse

from django.views.decorators.csrf import csrf_exempt

def index(request):
    return render(request,'index.html')

#def about(request):
 #   return HttpResponse("about")

def contact(request):
    return render(request,'contactUs.html')

@csrf_exempt
def Uregister(request):
    if request.method == "POST":
        # request.session["teamname"]=request.POST.get('teamname')
        # request.session["domains"]=request.POST.get('domains')
        # request.session["teamsize"]=request.POST.get('teamsize')

        teamname=request.POST.get('teamname')
        domains=request.POST.get('domains')
        teamsize=request.POST.get('teamsize')


        print(teamname)
        print(domains)
        print(teamsize)

        # request.session["leader_name"]=request.POST.get('leader_name')
        # request.session["leader_mail"]=request.POST.get('leader_mail')
        # request.session["leader_number"]=request.POST.get('leader_number')
        # request.session["leader_clg"]=request.POST.get('leader_clg')

        leader_name=request.POST.get('leader_name')
        leader_mail=request.POST.get('leader_mail')
        leader_number=request.POST.get('leader_number')
        leader_clg=request.POST.get('leader_clg')


        print(leader_name)
        print(leader_mail)
        print(leader_number)
        print(leader_clg)

        request.session["name1"]=request.POST.get('name1')
        request.session["mail1"]=request.POST.get('mail1')
        request.session["number1"]=request.POST.get('number1')
        request.session["clg1"]=request.POST.get('clg1')

        request.session["name2"]=request.POST.get('name2')
        request.session["mail2"]=request.POST.get('mail2')
        request.session["number2"]=request.POST.get('number2')
        request.session["clg2"]=request.POST.get('clg2')

        request.session["name3"]=request.POST.get('name3')
        request.session["mail3"]=request.POST.get('mail3')
        request.session["number3"]=request.POST.get('number3')
        request.session["clg3"]=request.POST.get('clg3')
        print(request.FILES)
        abstractPdf = request.FILES['Abstract']
        extra = domains(M1MailId = leader_mail,domainName=domains,abstract=abstractPdf)
        extra.save()
    else:
        return render(request,'registration.html')

def admins(request):
    return render(request,'adminVerify.html')

#def register1(request):
    
