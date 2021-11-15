from django.contrib.auth.models import User,auth
from django.http import request
from django.shortcuts import  render, redirect
from django.contrib.auth import login, authenticate
from django.contrib import messages
from django.contrib.auth.forms import AuthenticationForm 
from django.core.validators import MinLengthValidator
from django.views import View
from .models import *
from datetime import datetime, timedelta
import time
from .models import *

# Create your views here.
# USE GET not iteration in html but filter needed

def homepage(request):
	return render(request,"homepage.html")

def new_search(request):
	return render(request,"flight.html")

def register_request(request):
	'''from_class = NewUserForm
	template_name = 'register' '''
	if request.method == 'POST':
		username = request.POST['username']
		password1 = request.POST['password1']
		password2 = request.POST['password2']
		if User.objects.filter(username=username).exists():
				# messages.info(request,'This username has already been taken!')
				print("This username has already been taken!")
				return render(request,'register.html',{'message1':"This username has already been taken"})
		else:
			if password1==password2:
			    regis = User.objects.create_user(username=username,password=password1)
			    regis.save()
			    print("user created")
			else:
				# messages.info(request, 'Password is not match!')
				print("Password is not match!")
				return render(request,'register.html',{'message2':"Password is not match!"})
		return redirect('/')
	else:
		return render(request,'register.html')

def login_request(request):
	if request.method=='POST':
		username = request.POST['username']
		password = request.POST['password']
		user = auth.authenticate(username=username,password=password)
		if user is not None:
			auth.login(request,user)
			messages.success(request, f" Hello {username}, You Are Successfully Logged In")
			return render(request,"flight.html")
			# if user.is_active: 
			# 	request.session.set_expiry(86400)
			# 	login(request,user)
			# 	messages.success(request, f" Hello {username}, You Are Successfully Logged In")
			# 	return render(request,"flight.html")
		else:
			if not User.objects.filter(username=username).exists():
				messages.error(request, "Username Doesn't Exist")
				return render(request,'homepage.html',{'message3':"Username Doesn't Exist."})
				
			else:
				messages.info(request, "Incorrect Password")
				return render(request,'homepage.html',{'message4':"Incorrect Password."})
			return redirect('homepage')
	else:
		return render(request,'homepage.html')

def logout(request):
	try:
		del request.session['username']
	except KeyError:
		pass
	return redirect('/')

def search(request):
	if request.method=="POST":
		origin = request.POST['origin']
		destination = request.POST['destination']
		origin_2 = request.POST['origin2']
		destination_2 = request.POST['destination2']
		seatclass = request.POST['seatclass']
		seatclass2 = request.POST['seatclass2']
		departdate1 = request.POST['depart_date1']
		departdate2 = request.POST['depart_date2']
		trip_type = request.POST['TripType']
		print(trip_type)
		if(trip_type=="2"):
			origin2 = destination_2
			destination2 = origin_2
			returndate = request.POST['return_date']
			ticket1 = Ticket.objects.filter(
				origin__code=origin_2,
				destination__code=destination_2,
				seat_class=seatclass2,
				depart_date=departdate2,
			)
			print(ticket1)
			print("2",origin2,destination2,trip_type)
			return render(request,"search.html",{'ticket1':ticket1,
				'origin2':origin2,
				'trip_type':trip_type,
				'destination2':destination2,
				'return_date':returndate
				})
		elif(trip_type=="1"):
			print(origin,destination,seatclass,departdate1)
			ticket = Ticket.objects.filter(
				origin__code=origin,
				destination__code=destination,
				seat_class = seatclass,
				depart_date = departdate1
			)
			print(ticket)
			print("1",origin,destination,trip_type)
			return render(request,"search.html",{'ticket':ticket,'trip_type':trip_type,
				'origin':origin,
				'destination':destination
			})
	return render(request,"search.html")

def review(request):
	# One-way
	if "book" in request.POST:
		origin_book = request.POST.get('origin_book')
		destination_book = request.POST.get('destination_book')
		flightnumber_book = request.POST.get('flightnumber_book')
		print(flightnumber_book)
		ticket = Ticket.objects.get(
				fnumber = flightnumber_book
		)
		print(origin_book,destination_book,ticket)
		content1 = {
			'ticket_review':ticket,
			'trip_type':"1"
		}
		return render(request,"review.html",content1)
	# Round trip
	elif "book1" in request.POST:
		# ขาไป
		origin_book1 = request.POST.get('origin_book1')
		destination_book1 = request.POST.get('destination_book1')
		flightnumber_book1 = request.POST.get('flightnumber_book1')
		ticket1 = Ticket.objects.filter(
			origin__city = origin_book1,
			destination__city = destination_book1,
			fnumber = flightnumber_book1
		)
		# ขากลับ
		origin_book2 = request.POST.get('origin_book2')
		destination_book2 = request.POST.get('destination_book2')
		return_date_book2 = request.POST.get('return_date_book2') # to depart date
		seat_class_book2 = request.POST.get('seat_class_book2')
		ticket2 = Ticket.objects.filter(
			origin__code = origin_book2,
			destination__code = destination_book2,
			depart_date = return_date_book2,
			seat_class = seat_class_book2
		)
		content2 = {
			'origin_book1':origin_book1,
			'destination_book1':destination_book1,
			'flightnumber_book1':flightnumber_book1,
			'ticket2':ticket2,
			'ticket1':ticket1
		}
		return render(request,"search_return.html",content2)
	return render(request,"review.html")

def review2(request):
	if request.method=="POST":
		fnumber_depart_booked = request.POST.get('fnumber_depart_booked')
		origin_book2 = request.POST.get('origin_book2')
		destination_book2 = request.POST.get('destination_book2')
		flightnumber_book2 = request.POST.get('flightnumber_book2')
		# Depart
		ticket1 = Ticket.objects.get(fnumber=fnumber_depart_booked)
		# Return
		ticket2 = Ticket.objects.get(fnumber=flightnumber_book2)
		content = {
			'ticket1': ticket1,
			'ticket2': ticket2,
			'total_fare': ticket2.fare + ticket1.fare
		}
		return render(request,"review.html",content)