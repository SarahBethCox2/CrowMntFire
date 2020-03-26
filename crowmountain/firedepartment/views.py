from django.shortcuts import render
from .models import Citizen
from .models import Volunteer
from django.shortcuts import redirect
#Sendgrid imports
import os
#from sendgrid import SendGridAPIClient
#from sendgrid.helpers.mail import Mail
#####################################

# Create your views here.
def index(request):
    return render(request, 'pages/home.html')

def aboutus(request):
    return render(request, 'pages/aboutus.html')

def contactus(request):
    return render(request, 'pages/contactus.html')

def volunteer(request):
    #print(request.POST.get('errormsg'))

    #if request.POST.get("came_from")=="updateform":
        #firstname = request.POST.get("firstName")
        #lastname = request.POST.get("lastName")
        #address = request.POST.get("volunteerAddress")
        #age = request.POST.get("age")
        #phone = request.POST.get("phoneNumber")
        #email = request.POST.get("email")
        #volunteerid =request.POST.get("volunteerid")
        #Citizen.objects.filter(VolunteerID=volunteerid).update(First_Name=firstname, Last_Name=lastname, Phone=phone, Address=address,Age=age, Email=email)

        return render(request, 'pages/volunteer.html')
        
        

   #elif request.POST.get("came_from")=="volunteerform":
    #    firstname = request.POST.get("firstName")
     #   lastname = request.POST.get("lastName")
      #  address = request.POST.get("volunteerAddress")
       # city = request.POST.get("city")
        #zipcode = request.POST.get("zipCode")
        #age = request.POST.get("age")
        #phone = request.POST.get("phoneNumber")
        #email = request.POST.get("email")
        
        #fulladdress = address + " " + city + ", AR " + zipcode
       # citizendata = Citizen(First_Name=firstname, Last_Name=lastname, Phone=phone, Address=fulladdress,Age=age, Email=email)

        #citizendata.save()
        #citizen = citizendata

        #volunterdata = Volunteer(Citizen=citizen, Acceptance_Status="Accepted")
        #volunterdata.save()
       
        #message = Mail(
        #from_email=email,
        #to_emails='hescalante@atu.edu',
        #subject='New Volunteer',
        #html_content='<strong>Hola</strong>')
        #try:
            #sg = SendGridAPIClient(os.environ.get('SENDGRID_API_KEY'))
            #response = sg.send(message)
            #status = response.status_code
            #return render(request, 'pages/volunteer/volunteer.html', {'status':status, 'email':email})
            
        #except Exception as e:
            #print(e)

    #elif request.POST.get("came_from")=="volunteerIDForm":
        #print("from same s")
        #citizens = Citizen.objects.all()
        #vid=request.POST.get("volunteerID")
        #try:
            #volunteer = citizens.get(VolunteerID=vid)
        #except Exception as e:
            # return render(request, 'pages/volunteer/volunteer.html', {"errormsg":"Invalid ID"})
    
        #return render(request, 'pages/volunteer/update.html', {'volunteer':volunteer})


   #return render(request, 'pages/volunteer/volunteer.html')

def volunteerform(request):
    return render(request, 'pages/volunteer/form.html')

def updateform(request):
    return render(request, 'pages/volunteer/update.html', {'volunteer':volunteer})

def burnnotice(request):
    return render(request, 'pages/burnnotice/burnnotice.html')

def events(request):
    return render(request, 'pages/events.html')

def educational(request):
    return render(request,'pages/educational.html')