# from django.shortcuts import render
# import re
# from django.utils.timezone import datetime

# # Create your views here.
# from django.http import HttpResponse

# def home(request):
#     return HttpResponse("Hello, Django!")


# # def hello_there(request, name):
# #     now = datetime.now()
# #     formatted_now = now.strftime("%A, %d %B, %Y at %X")

# #     # Filter the name argument to letters only using regular expressions. URL arguments
# #     # can contain arbitrary text, so we restrict to safe characters only.
# #     match_object = re.match("[a-zA-Z]+", name)

# #     if match_object:
# #         clean_name = match_object.group(0)
# #     else:
# #         clean_name = "Friend


# #     content = "Hello there, " + clean_name + "! It's " + formatted_now
# #     return HttpResponse(content)
# def hello_there(request, name):
#     return render(
#         request,
#         'covidpred/hello_there.html',
#         {
#             'name': name,
#             'date': datetime.now()
#         }
#     )
from django.shortcuts import render, redirect
from django.contrib import messages
from django.contrib.auth import authenticate, login
from django.contrib.auth.decorators import login_required
from django.contrib.auth.forms import AuthenticationForm
from . forms import UserRegisterForm
from django.core.mail import send_mail
from django.core.mail import EmailMultiAlternatives
from django.template.loader import get_template
from django.template import Context
import joblib 
# import time 
# import datetime 
# import smtplib 

#################### index#######################################
def index(request):
	return render(request, 'covidpred/index.html', {'title': 'index'})

########### register here #####################################


def register(request):
	if request.method == 'POST':
		form = UserRegisterForm(request.POST)
		if form.is_valid():
			form.save()
			username = form.cleaned_data.get('username')
			email = form.cleaned_data.get('email')
			######################### mail system ####################################
			htmly = get_template('covidpred/Email.html')
			d = {'username': username}
			subject, from_email, to = 'welcome', '2018.anjali.hassani@ves.ac.in', email
			html_content = htmly.render(d)
			msg = EmailMultiAlternatives(subject, html_content, from_email, [to])
			msg.attach_alternative(html_content, "text/html")
			msg.send()
			##################################################################
			messages.success(
				request, f'Your account has been created ! You are now able to log in')
			return redirect('login')
	else:
		form = UserRegisterForm()
	return render(request, 'covidpred/register.html', {'form': form, 'title': 'reqister here'})

################ login forms###################################################


def Login(request):
	if request.method == 'POST':

		# AuthenticationForm_can_also_be_used__

		username = request.POST['username']
		password = request.POST['password']
		user = authenticate(request, username=username, password=password)
		if user is not None:
			form = login(request, user)
			messages.success(request, f' wecome {username} !!')
			return redirect('index')
		else:
			messages.info(request, f'account done not exit plz sign in')
	form = AuthenticationForm()
	return render(request, 'covidpred/login.html', {'form': form, 'title': 'log in'})


def result(request):
	cls=joblib.load('covid_model.sav')
	
	lis=[]
	lis.append(request.GET['Breathing Problem'])
	lis.append(request.GET['Fever'])	
	lis.append(request.GET['Dry Cough'])
	lis.append(request.GET['Sore throat'])
	lis.append(request.GET['Running Nose'])	
	lis.append(request.GET['Asthma'])	
	lis.append(request.GET['Chronic Lung Disease'])
	lis.append(request.GET['Headache'])
	lis.append(request.GET['Heart Disease'])
	lis.append(request.GET['Diabetes'])
	lis.append(request.GET['Hyper Tension'])
	lis.append(request.GET['Fatigue '])
	lis.append(request.GET[ 'Gastrointestinal '])

	lis.append(request.GET['Abroad travel'])
	lis.append(request.GET['Contact with COVID Patient'])
	lis.append(request.GET['Attended Large Gathering'])	
	lis.append(request.GET['Visited Public Exposed Places'])
	lis.append(request.GET['Family working in Public Exposed Places'])
	
	print(lis)
	ans=cls.predict([lis])
	print(ans)
	print(type(ans))
	result = ans[0]
	print(result)
	return render(request, 'covidpred/result.html',{'ans': result})

def about(request):
	return render(request,"covidpred/about_us.html")

# def mail(request):
# 	if result==1:
# 		unix=int(time.time()) 
# 		time1= str(datetime.datetime.fromtimestamp(unix)strftime('%I:%M:%S:%p'))  
# 		if time1 =='03:00:00:PM':
# 			gmailaddress = '2018.anjali.hassani@ves.ac.in'
# 			email = form.cleaned_data.get('email')
# 			gmailpassword = 'Anjali@1234#'
# 			mailto = email
# 			SUBJECT='reminder to check SPO2 levels'
# 			msg='Hello , This is a reminder message for you to check your spo2 levels.'
# 			message = 'Subject: {}\n\n{}'.format(SUBJECT, msg)
# 			mailServer = smtplib.SMTP('smtp.gmail.com' , 587)
# 			mailServer.starttls()
# 			mailServer.login(gmailaddress , gmailpassword)
# 			mailServer.sendmail(gmailaddress, mailto , message)
# 			print(" \n Sent!")
# 			mailServer.quit()



# htmly = get_template('covidpred/Email.html')
# 			d = {'username': username}
# 			subject, from_email, to = 'welcome', '2018.anjali.hassani@ves.ac.in', email
# 			html_content = htmly.render(d)
# 			msg = EmailMultiAlternatives(subject, html_content, from_email, [to])
# 			msg.attach_alternative(html_content, "text/html")
# 			msg.send()
