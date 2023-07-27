from django.shortcuts import render,redirect
from .models import HomeEducator
from .models import HomeEducator,OutsideEducator,HomeEducatorSubjects,OutsideEducatorSubjects,TemporaryE
from django.db.models import Q
from django.contrib import messages

def educatorAuthication(request):
    return render(request,'educator/authication.html')



def hEducatorSignup(request):

    if request.method == 'GET':
        return render(request, "educator/hEducatorSignup.html")

    else:
        username = request.POST["username"]
        email = request.POST["email"]
        university = request.POST["university"]
        department = request.POST["department"]
        experience = request.POST["experience"]
        location = request.POST["location"]
        contact = request.POST["contact"]
        password = request.POST["password"]
        password_repeat = request.POST["password_repeat"]

        if password == password_repeat:
            if HomeEducator.objects.filter(homeTutorName=username).exists():
                messages.info(request, "Username Already Taken")
                return redirect('heducatorsignup')
            elif HomeEducator.objects.filter(homeTutorEmail=email).exists():
                messages.info(request, "Email Already Taken")
                return redirect('heducatorsignup')
            elif university=="" or department=="" or experience=="" or contact=="":
                messages.info(request, "Empty fields")
                return redirect('heducatorsignup')
            else:
                homeEducator_info = HomeEducator(homeTutorName=username, homeTutorEmail=email,
                                                 university=university, department=department,
                                                 experience=experience, homeTutorLocation=location,
                                                 homeTutorContact=contact, homeTutorPassword=password,
                                                 homeTutorRating=0.0)

                homeEducator_info.save()
                return redirect("subjectchoicehome")

        else:
            messages.info(request, "password not match")
            return redirect('heducatorsignup')


def oEducatorSignup(request):

    if request.method == 'GET':
        return render(request, "educator/oEducatorSignup.html")

    else:
        username = request.POST["username"]
        email = request.POST["email"]
        institute = request.POST["institute"]
        designation = request.POST["designation"]
        location = request.POST["location"]
        contact = request.POST["contact"]
        password = request.POST["password"]
        password_repeat = request.POST["password_repeat"]

        if password == password_repeat:
            if OutsideEducator.objects.filter(outsideTutorName=username).exists():
                messages.info(request, "Username Already Taken")
                return redirect('oeducatorsignup')
            elif OutsideEducator.objects.filter(outsideTutorEmail=email).exists():
                messages.info(request, "Email Already Taken")
                return redirect('oeducatorsignup')
            elif institute=="" or designation=="" or contact=="":
                messages.info(request, "Empty fields")
                return redirect('oeducatorsignup')
            else:
                outsideEducator_info = OutsideEducator(outsideTutorName=username, outsideTutorEmail=email,
                                                       institute=institute, designation=designation,
                                                       outsideTutorLocation=location, outsideTutorContact=contact,
                                                       outsideTutorPassword=password,outsideTutorRating=0.0)

                outsideEducator_info.save()
                return redirect("subjectchoiceoutside")

        else:
            messages.info(request, "password not match")
            return redirect('oeducatorsignup')


def educatorLogin(request):
    if request.method == 'POST':
        username = request.POST['username']
        educatorType = request.POST['educatorType']
        password = request.POST['password']

        if educatorType == "Outside Educator":
            if OutsideEducator.objects.filter(outsideTutorName=username).exists():
                if OutsideEducator.objects.filter(outsideTutorPassword=password).exists():

                    oeducator = OutsideEducator.objects.filter(Q(outsideTutorName=username) & Q(outsideTutorPassword=password))

                    temporary_info = TemporaryE(id=1, tutorName=username, tutorPassword=password, tutorType=educatorType)
                    temporary_info.save()

                    context = {"oeducator": oeducator}
                    return render(request, 'educator/educatorProfile.html', context)

                else:
                    messages.info(request,"Invalid Password")
                    return redirect("login")
            else:
                messages.info(request, "Invalid Username")
                return redirect("login")

        else:
            if HomeEducator.objects.filter(homeTutorName=username).exists():
                if HomeEducator.objects.filter(homeTutorPassword=password).exists():

                    heducator = HomeEducator.objects.filter(Q(homeTutorName=username) & Q(homeTutorPassword=password))

                    temporary_info = TemporaryE(id=1, tutorName=username, tutorPassword=password, tutorType=educatorType)
                    temporary_info.save()

                    context = {"heducator": heducator}
                    return render(request, 'educator/educatorProfile.html', context)

                else:
                    messages.info(request,"Invalid Password")
                    return redirect("login")
            else:
                messages.info(request, "Invalid Username")
                return redirect("login")

    else:
        return render(request,'educator/login.html')


def educatorProfile(request):

    x = TemporaryE.objects.get(id=1)

    if OutsideEducator.objects.filter(Q(outsideTutorName=x.tutorName) & Q(outsideTutorPassword=x.tutorPassword)).exists():

        oeducator = OutsideEducator.objects.filter(Q(outsideTutorName=x.tutorName) & Q(outsideTutorPassword=x.tutorPassword))
        context = {"oeducator": oeducator}

    else:
        heducator = HomeEducator.objects.filter(Q(homeTutorName=x.tutorName) & Q(homeTutorPassword=x.tutorPassword))
        context = {"heducator": heducator}

    return render(request,'educator/educatorProfile.html',context)


def educatorLogout(request):

    x = TemporaryE.objects.get(id=1)
    x.delete()

    return render(request,'educator/educatorlogout.html')


def educatorUpdateInfo(request):
    if request.method == 'POST':
        email = request.POST['email']
        location = request.POST['location']
        contact = request.POST['contact']
        password = request.POST['password']
        password_repeat = request.POST['password_repeat']

        if email!='' and location!='' and contact!='' and password!='' and password==password_repeat:

            x = TemporaryE.objects.get(id=1)

            if HomeEducator.objects.filter(Q(homeTutorName=x.tutorName) & Q(homeTutorPassword=x.tutorPassword)).exists():
                heducator = HomeEducator.objects.get(Q(homeTutorName=x.tutorName) & Q(homeTutorPassword=x.tutorPassword))
                heducator.homeTutorEmail = email
                heducator.homeTutorLocation = location
                heducator.homeTutorContact = contact
                heducator.homeTutorPassword = password
                x.tutorPassword = password
                heducator.save()
                x.save()

                messages.info(request, "All info updated")
                return render(request, 'educator/educatorUpdateInfo.html')

            else:
                oeducator = OutsideEducator.objects.get(Q(outsideTutorName=x.tutorName) & Q(outsideTutorPassword=x.tutorPassword))
                oeducator.outsideTutorEmail = email
                oeducator.outsideTutorLocation = location
                oeducator.outsideTutorContact = contact
                oeducator.outsideTutorPassword = password
                x.tutorPassword = password
                oeducator.save()
                x.save()

                messages.info(request, "All info updated")
                return render(request, 'educator/educatorUpdateInfo.html')

        elif email!='' and location!='None' and contact!='' and password!='' and password!=password_repeat:
            messages.info(request,"Password not match")
            return render(request, 'educator/educatorUpdateInfo.html')

        elif email!='' and location=='None' and contact=='' and password=='':

            x = TemporaryE.objects.get(id=1)

            if HomeEducator.objects.filter(Q(homeTutorName=x.tutorName) & Q(homeTutorPassword=x.tutorPassword)).exists():
                heducator = HomeEducator.objects.get(Q(homeTutorName=x.tutorName) & Q(homeTutorPassword=x.tutorPassword))
                heducator.homeTutorEmail = email
                heducator.save()

                messages.info(request,"Email updated")
                return render(request, 'educator/educatorUpdateInfo.html')

            else:
                oeducator = OutsideEducator.objects.get(Q(outsideTutorName=x.tutorName) & Q(outsideTutorPassword=x.tutorPassword))
                oeducator.outsideTutorEmail = email
                oeducator.save()

                messages.info(request,"Email updated")
                return render(request, 'educator/educatorUpdateInfo.html')

        elif email=='' and location!='None' and contact=='' and password=='':

            x = TemporaryE.objects.get(id=1)

            if HomeEducator.objects.filter(Q(homeTutorName=x.tutorName) & Q(homeTutorPassword=x.tutorPassword)).exists():
                heducator = HomeEducator.objects.get(Q(homeTutorName=x.tutorName) & Q(homeTutorPassword=x.tutorPassword))
                heducator.homeTutorLocation = location
                heducator.save()

                messages.info(request,"Location updated")
                return render(request, 'educator/educatorUpdateInfo.html')

            else:
                oeducator = OutsideEducator.objects.get(Q(outsideTutorName=x.tutorName) & Q(outsideTutorPassword=x.tutorPassword))
                oeducator.outsideTutorLocation = location
                oeducator.save()

                messages.info(request,"Location updated")
                return render(request, 'educator/educatorUpdateInfo.html')

        elif email=='' and location=='None' and contact!='' and password=='':

            x = TemporaryE.objects.get(id=1)

            if HomeEducator.objects.filter(Q(homeTutorName=x.tutorName) & Q(homeTutorPassword=x.tutorPassword)).exists():
                heducator = HomeEducator.objects.get(Q(homeTutorName=x.tutorName) & Q(homeTutorPassword=x.tutorPassword))
                heducator.homeTutorContact = contact
                heducator.save()

                messages.info(request,"Contact updated")
                return render(request, 'educator/educatorUpdateInfo.html')

            else:
                oeducator = OutsideEducator.objects.get(Q(outsideTutorName=x.tutorName) & Q(outsideTutorPassword=x.tutorPassword))
                oeducator.outsideTutorContact = contact
                oeducator.save()

                messages.info(request,"Contact updated")
                return render(request, 'educator/educatorUpdateInfo.html')

        elif email=='' and location=='None' and contact=='' and password!='' and password==password_repeat:

            x = TemporaryE.objects.get(id=1)

            if HomeEducator.objects.filter(Q(homeTutorName=x.tutorName) & Q(homeTutorPassword=x.tutorPassword)).exists():
                heducator = HomeEducator.objects.get(Q(homeTutorName=x.tutorName) & Q(homeTutorPassword=x.tutorPassword))
                heducator.homeTutorPassword = password
                x.tutorPassword = password
                heducator.save()
                x.save()

                messages.info(request,"Password updated")
                return render(request, 'educator/educatorUpdateInfo.html')

            else:
                oeducator = OutsideEducator.objects.get(Q(outsideTutorName=x.tutorName) & Q(outsideTutorPassword=x.tutorPassword))
                oeducator.outsideTutorPassword = password
                x.tutorPassword = password
                oeducator.save()
                x.save()

                messages.info(request,"Password updated")
                return render(request, 'educator/educatorUpdateInfo.html')

        elif email!='' and location=='None' and contact!='' and password=='':

            x = TemporaryE.objects.get(id=1)

            if HomeEducator.objects.filter(Q(homeTutorName=x.tutorName) & Q(homeTutorPassword=x.tutorPassword)).exists():
                heducator = HomeEducator.objects.get(Q(homeTutorName=x.tutorName) & Q(homeTutorPassword=x.tutorPassword))
                heducator.homeTutorEmail = email
                heducator.homeTutorContact = contact
                heducator.save()

                messages.info(request,"Email & Contact updated")
                return render(request, 'educator/educatorUpdateInfo.html')

            else:
                oeducator = OutsideEducator.objects.get(Q(outsideTutorName=x.tutorName) & Q(outsideTutorPassword=x.tutorPassword))
                oeducator.outsideTutorEmail = email
                oeducator.outsideTutorContact = contact
                oeducator.save()

                messages.info(request,"Email & Contact updated")
                return render(request, 'educator/educatorUpdateInfo.html')

        elif email=='' and location!='None' and contact!='' and password=='':

            x = TemporaryE.objects.get(id=1)

            if HomeEducator.objects.filter(Q(homeTutorName=x.tutorName) & Q(homeTutorPassword=x.tutorPassword)).exists():
                heducator = HomeEducator.objects.get(Q(homeTutorName=x.tutorName) & Q(homeTutorPassword=x.tutorPassword))
                heducator.homeTutorLocation = location
                heducator.homeTutorContact = contact
                heducator.save()

                messages.info(request,"Location & Contact updated")
                return render(request, 'educator/educatorUpdateInfo.html')

            else:
                oeducator = OutsideEducator.objects.get(Q(outsideTutorName=x.tutorName) & Q(outsideTutorPassword=x.tutorPassword))
                oeducator.outsideTutorLocation = location
                oeducator.outsideTutorContact = contact
                oeducator.save()

                messages.info(request,"Location & Contact updated")
                return render(request, 'educator/educatorUpdateInfo.html')

        elif email!='' and location!='None' and contact=='' and password=='':

            x = TemporaryE.objects.get(id=1)

            if HomeEducator.objects.filter(Q(homeTutorName=x.tutorName) & Q(homeTutorPassword=x.tutorPassword)).exists():
                heducator = HomeEducator.objects.get(Q(homeTutorName=x.tutorName) & Q(homeTutorPassword=x.tutorPassword))
                heducator.homeTutorEmail = email
                heducator.homeTutorLocation = location
                heducator.save()

                messages.info(request,"Email & Location updated")
                return render(request, 'educator/educatorUpdateInfo.html')

            else:
                oeducator = OutsideEducator.objects.get(Q(outsideTutorName=x.tutorName) & Q(outsideTutorPassword=x.tutorPassword))
                oeducator.outsideTutorEmail = email
                oeducator.outsideTutorLocation = location
                oeducator.save()

                messages.info(request,"Email & Location updated")
                return render(request, 'educator/educatorUpdateInfo.html')

        elif email!='' and location!='None' and contact!='' and password=='':

            x = TemporaryE.objects.get(id=1)

            if HomeEducator.objects.filter(Q(homeTutorName=x.tutorName) & Q(homeTutorPassword=x.tutorPassword)).exists():
                heducator = HomeEducator.objects.get(Q(homeTutorName=x.tutorName) & Q(homeTutorPassword=x.tutorPassword))
                heducator.homeTutorEmail = email
                heducator.homeTutorLocation = location
                heducator.homeTutorContact = contact
                heducator.save()

                messages.info(request,"Email, Location & Contact updated")
                return render(request, 'educator/educatorUpdateInfo.html')

            else:
                oeducator = OutsideEducator.objects.get(Q(outsideTutorName=x.tutorName) & Q(outsideTutorPassword=x.tutorPassword))
                oeducator.outsideTutorEmail = email
                oeducator.outsideTutorLocation = location
                oeducator.outsideTutorContact = contact
                oeducator.save()

                messages.info(request,"Email, Location & Contact updated")
                return render(request, 'educator/educatorUpdateInfo.html')

        elif email!='' and location=='None' and contact=='' and password!='' and password==password_repeat:

            x = TemporaryE.objects.get(id=1)

            if HomeEducator.objects.filter(Q(homeTutorName=x.tutorName) & Q(homeTutorPassword=x.tutorPassword)).exists():
                heducator = HomeEducator.objects.get(Q(homeTutorName=x.tutorName) & Q(homeTutorPassword=x.tutorPassword))
                heducator.homeTutorEmail = email
                heducator.homeTutorPassword = password
                x.tutorPassword = password
                heducator.save()
                x.save()

                messages.info(request,"Email & Password updated")
                return render(request, 'educator/educatorUpdateInfo.html')

            else:
                oeducator = OutsideEducator.objects.get(Q(outsideTutorName=x.tutorName) & Q(outsideTutorPassword=x.tutorPassword))
                oeducator.outsideTutorEmail = email
                oeducator.outsideTutorPassword = password
                x.tutorPassword = password
                oeducator.save()
                x.save()

                messages.info(request,"Email & Password updated")
                return render(request, 'educator/educatorUpdateInfo.html')

        elif email == '' and location != 'None' and contact == '' and password != '' and password == password_repeat:

            x = TemporaryE.objects.get(id=1)

            if HomeEducator.objects.filter(
                    Q(homeTutorName=x.tutorName) & Q(homeTutorPassword=x.tutorPassword)).exists():
                heducator = HomeEducator.objects.get(
                    Q(homeTutorName=x.tutorName) & Q(homeTutorPassword=x.tutorPassword))
                heducator.homeTutorLocation = location
                heducator.homeTutorPassword = password
                x.tutorPassword = password
                heducator.save()
                x.save()

                messages.info(request, "Location & Password updated")
                return render(request, 'educator/educatorUpdateInfo.html')

            else:
                oeducator = OutsideEducator.objects.get(
                    Q(outsideTutorName=x.tutorName) & Q(outsideTutorPassword=x.tutorPassword))
                oeducator.outsideTutorEmail = email
                oeducator.outsideTutorPassword = password
                x.tutorPassword = password
                oeducator.save()
                x.save()

                messages.info(request, "Location & Password updated")
                return render(request, 'educator/educatorUpdateInfo.html')

        elif email == '' and location == 'None' and contact != '' and password != '' and password == password_repeat:

            x = TemporaryE.objects.get(id=1)

            if HomeEducator.objects.filter(
                    Q(homeTutorName=x.tutorName) & Q(homeTutorPassword=x.tutorPassword)).exists():
                heducator = HomeEducator.objects.get(
                    Q(homeTutorName=x.tutorName) & Q(homeTutorPassword=x.tutorPassword))
                heducator.homeTutorContact = contact
                heducator.homeTutorPassword = password
                x.tutorPassword = password
                heducator.save()
                x.save()

                messages.info(request, "Contact & Password updated")
                return render(request, 'educator/educatorUpdateInfo.html')

            else:
                oeducator = OutsideEducator.objects.get(
                    Q(outsideTutorName=x.tutorName) & Q(outsideTutorPassword=x.tutorPassword))
                oeducator.outsideTutorContact = contact
                oeducator.outsideTutorPassword = password
                x.tutorPassword = password
                oeducator.save()
                x.save()

                messages.info(request, "Contact & Password updated")
                return render(request, 'educator/educatorUpdateInfo.html')

        elif email != '' and location != 'None' and contact == '' and password != '' and password == password_repeat:

            x = TemporaryE.objects.get(id=1)

            if HomeEducator.objects.filter(
                    Q(homeTutorName=x.tutorName) & Q(homeTutorPassword=x.tutorPassword)).exists():
                heducator = HomeEducator.objects.get(
                    Q(homeTutorName=x.tutorName) & Q(homeTutorPassword=x.tutorPassword))
                heducator.homeTutorEmail = email
                heducator.homeTutorLocation = location
                heducator.homeTutorPassword = password
                x.tutorPassword = password
                heducator.save()
                x.save()

                messages.info(request, "Email, Location & Password updated")
                return render(request, 'educator/educatorUpdateInfo.html')

            else:
                oeducator = OutsideEducator.objects.get(
                    Q(outsideTutorName=x.tutorName) & Q(outsideTutorPassword=x.tutorPassword))
                oeducator.outsideTutorEmail = email
                oeducator.outsideTutorPassword = password
                oeducator.outsideTutorLocation = location
                x.tutorPassword = password
                oeducator.save()
                x.save()

                messages.info(request, "Email, Location & Password updated")
                return render(request, 'educator/educatorUpdateInfo.html')

        elif email != '' and contact != '' and password != '' and password == password_repeat:

            x = TemporaryE.objects.get(id=1)

            if HomeEducator.objects.filter(
                    Q(homeTutorName=x.tutorName) & Q(homeTutorPassword=x.tutorPassword)).exists():
                heducator = HomeEducator.objects.get(
                    Q(homeTutorName=x.tutorName) & Q(homeTutorPassword=x.tutorPassword))
                heducator.homeTutorEmail = email
                heducator.homeTutorContact = contact
                heducator.homeTutorPassword = password
                x.tutorPassword = password
                heducator.save()
                x.save()

                messages.info(request, "Email, Contact & Password updated")
                return render(request, 'educator/educatorUpdateInfo.html')

            else:
                oeducator = OutsideEducator.objects.get(
                    Q(outsideTutorName=x.tutorName) & Q(outsideTutorPassword=x.tutorPassword))
                oeducator.outsideTutorEmail = email
                oeducator.outsideTutorContact = contact
                oeducator.outsideTutorPassword = password
                x.tutorPassword = password
                oeducator.save()
                x.save()

                messages.info(request, "Email, Contact & Password updated")
                return render(request, 'educator/educatorUpdateInfo.html')

        elif email == '' and location != 'None' and contact != '' and password != '' and password == password_repeat:

            x = TemporaryE.objects.get(id=1)

            if HomeEducator.objects.filter(
                    Q(homeTutorName=x.tutorName) & Q(homeTutorPassword=x.tutorPassword)).exists():
                heducator = HomeEducator.objects.get(
                    Q(homeTutorName=x.tutorName) & Q(homeTutorPassword=x.tutorPassword))
                heducator.homeTutorContact = contact
                heducator.homeTutorLocation = location
                heducator.homeTutorPassword = password
                x.tutorPassword = password
                heducator.save()
                x.save()

                messages.info(request, "Contact, Location & Password updated")
                return render(request, 'educator/educatorUpdateInfo.html')

            else:
                oeducator = OutsideEducator.objects.get(
                    Q(outsideTutorName=x.tutorName) & Q(outsideTutorPassword=x.tutorPassword))
                oeducator.outsideTutorContact = contact
                oeducator.outsideTutorPassword = password
                oeducator.outsideTutorLocation = location
                x.tutorPassword = password
                oeducator.save()
                x.save()

                messages.info(request, "Contact, Location & Password updated")
                return render(request, 'educator/educatorUpdateInfo.html')

        else:
            messages.info(request, "Info not update")
            return render(request, 'educator/educatorUpdateInfo.html')

    else:
        return render(request, 'educator/educatorUpdateInfo.html')


def subjectChoiceHome(request):

    if request.method == 'POST':
        firstSubject = request.POST['first']
        secondSubject = request.POST['second']
        thirdSubject = request.POST['third']

        if firstSubject=="None" and secondSubject=="None" and thirdSubject=="None":
            messages.info(request, "You didn't choice any subject")
            return redirect("subjectchoicehome")

        elif firstSubject!="None" and secondSubject!="None" and thirdSubject=="None":
            hSubject_info = HomeEducatorSubjects(firstSubject=firstSubject,secondSubject=secondSubject)
            hSubject_info.save()
            return redirect("login")

        elif firstSubject!="" and secondSubject=="None" and thirdSubject=="None":
            hSubject_info = HomeEducatorSubjects(firstSubject=firstSubject)
            hSubject_info.save()
            return redirect("login")

        elif firstSubject!="None" and secondSubject!="None" and thirdSubject!="None":
            hSubject_info = HomeEducatorSubjects(firstSubject=firstSubject, secondSubject=secondSubject,
                                                 thirdSubject=thirdSubject)
            hSubject_info.save()
            return redirect("login")

        else:
            messages.info(request, "You have to choose it serially")
            return redirect("subjectchoicehome")

    else:
        return render(request,'educator/subjectHome.html')


def subjectChoiceOutside(request):

    if request.method == 'POST':
        firstSubject = request.POST['first']
        secondSubject = request.POST['second']
        thirdSubject = request.POST['third']

        if firstSubject=="None" and secondSubject=="None" and thirdSubject=="None":
            messages.info(request, "You didn't choice any subject")
            return redirect("subjectchoiceoutside")

        elif firstSubject!="None" and secondSubject!="None" and thirdSubject=="None":
            oSubject_info = OutsideEducatorSubjects(firstSubject=firstSubject,secondSubject=secondSubject)
            oSubject_info.save()
            return redirect("login")

        elif firstSubject!="" and secondSubject=="None" and thirdSubject=="None":
            oSubject_info = OutsideEducatorSubjects(firstSubject=firstSubject)
            oSubject_info.save()
            return redirect("login")

        elif firstSubject!="None" and secondSubject!="None" and thirdSubject!="None":
            oSubject_info = OutsideEducatorSubjects(firstSubject=firstSubject, secondSubject=secondSubject,
                                                 thirdSubject=thirdSubject)
            oSubject_info.save()
            return redirect("login")

        else:
            messages.info(request, "You have to choose it serially")
            return redirect("subjectchoiceoutside")

    else:
        return render(request,'educator/subjectOutside.html')


        
