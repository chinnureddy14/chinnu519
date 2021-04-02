from django.shortcuts import render
from django.http import  HttpResponse

def home(request):
	return HttpResponse("<h1 style='background-color:powderblue;'>welcome to aits</h1>")

def chk(request):
	return HttpResponse("<script>alert('hi good afternoon')</script><h2>welcome</h2>")


def homepage(request):
	return render(request,'ht/homepage.html')


def lgn(re):
	return render(re,'ht/login.html')


def reg(rt):
	return render(rt,'ht/register.html') 


def bthm(qw):
	return render(qw,'ht/bthome.html')


def about(req):
	return render(req,'ht/about.html')

		
def contact(req):
	return render(req,'ht/contact.html')


def registration(req):
	if req.method=="POST":
		fn=req.POST['fname'];
		ln=req.POST['lname'];
		age=req.POST['age'];
		mail=req.POST['email'];
		pas=req.POST['pwd'];
		pas1=req.POST['pwd1'];
		d={'info':fn,'info1':ln,'info2':age,'info3':mail,'info4':pas,'info5':pas1}
		return render(req,'ht/details.html',{'d':d})
	return render(req,'ht/registration.html')


