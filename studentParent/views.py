from django.shortcuts import render,redirect
from .models import StudentParent,TemporarySP
from educator.models import HomeEducator,OutsideEducator,HomeEducatorSubjects,OutsideEducatorSubjects
from home.models import Request,Deals
from django.contrib import messages
from django.db.models import Q


def parentAuthication(request):
    return render(request,'studentParent/authication.html')





def parentSignUp(request):
    if request.method == 'GET':
        return render(request, "studentParent/signup.html")

    else:
        username = request.POST["username"]
        email = request.POST["email"]
        location = request.POST["location"]
        contact = request.POST["contact"]
        password = request.POST["password"]
        password_repeat = request.POST["password_repeat"]

        if password == password_repeat:
            if StudentParent.objects.filter(parentName=username).exists():
                messages.info(request, "Username Already Taken")
                return redirect('parentsignup')
            elif StudentParent.objects.filter(parentEmail=email).exists():
                messages.info(request, "Email Already Taken")
                return redirect('parentsignup')
            elif contact=="":
                messages.info(request, "Empty fields")
                return redirect('parentsignup')
            else:
                studentParent_info = StudentParent(parentName=username, parentEmail=email,
                                                    parentLocation=location, parentContact=contact,
                                                    parentPassword=password)

                studentParent_info.save()
                return redirect("parentlogin")

        else:
            messages.info(request, "password not match")
            return redirect('parentsignup')


def parentLogin(request):

    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']

        if StudentParent.objects.filter(parentName=username).exists():
            if StudentParent.objects.filter(parentPassword=password).exists():

                parent = StudentParent.objects.filter(Q(parentName=username) & Q(parentPassword=password))

                temporary_info = TemporarySP(id=1,parentName=username, parentPassword=password)
                temporary_info.save()

                context = {"parent": parent}
                return render(request,'studentParent/profileinfo.html',context)

            else:
                messages.info(request,"Invalid Password")
                return redirect("parentlogin")
        else:
            messages.info(request, "Invalid Username")
            return redirect("parentlogin")

    else:
        return render(request,'studentParent/parentlogin.html')


def profileInfo(request):

    x = TemporarySP.objects.get(id=1)
    parent = StudentParent.objects.filter(Q(parentName=x.parentName) & Q(parentPassword=x.parentPassword))
    context = {"parent": parent}

    return render(request,'studentParent/profileinfo.html',context)


def updateInfo(request):
    if request.method == 'POST':
        email = request.POST['email']
        location = request.POST['location']
        contact = request.POST['contact']
        password = request.POST['password']
        password_repeat = request.POST['password_repeat']

        if email!='' and location!='' and contact!='' and password!='' and password==password_repeat:
            x = TemporarySP.objects.get(id=1)
            parent = StudentParent.objects.get(Q(parentName=x.parentName) & Q(parentPassword=x.parentPassword))
            parent.parentEmail = email
            parent.parentLocation = location
            parent.parentContact = contact
            parent.parentPassword = password
            x.parentPassword = password
            parent.save()
            x.save()

            messages.info(request, "All info updated")
            return render(request, 'studentParent/updateinfo.html')

        elif email!='' and location!='None' and contact!='' and password!='' and password!=password_repeat:
            messages.info(request,"Password not match")
            return render(request, 'studentParent/updateinfo.html')

        elif email!='' and location=='None' and contact=='' and password=='':
            x = TemporarySP.objects.get(id=1)
            parent = StudentParent.objects.get(Q(parentName=x.parentName) & Q(parentPassword=x.parentPassword))
            parent.parentEmail = email
            parent.save()
            messages.info(request,"Email updated")
            return render(request, 'studentParent/updateinfo.html')

        elif email=='' and location!='None' and contact=='' and password=='':
            x = TemporarySP.objects.get(id=1)
            parent = StudentParent.objects.get(Q(parentName=x.parentName) & Q(parentPassword=x.parentPassword))
            parent.parentLocation = location
            parent.save()
            messages.info(request,"Location updated")
            return render(request, 'studentParent/updateinfo.html')

        elif email=='' and location=='None' and contact!='' and password=='':
            x = TemporarySP.objects.get(id=1)
            parent = StudentParent.objects.get(Q(parentName=x.parentName) & Q(parentPassword=x.parentPassword))
            parent.parentContact = contact
            parent.save()
            messages.info(request,"Contact updated")
            return render(request, 'studentParent/updateinfo.html')

        elif email=='' and location=='None' and contact=='' and password!='' and password==password_repeat:
            x = TemporarySP.objects.get(id=1)
            parent = StudentParent.objects.get(Q(parentName=x.parentName) & Q(parentPassword=x.parentPassword))
            parent.parentPassword = password
            x.parentPassword = password
            parent.save()
            x.save()
            messages.info(request,"Password updated")
            return render(request, 'studentParent/updateinfo.html')

        elif email!='' and location=='None' and contact=='' and password!='' and password==password_repeat:
            x = TemporarySP.objects.get(id=1)
            parent = StudentParent.objects.get(Q(parentName=x.parentName) & Q(parentPassword=x.parentPassword))
            parent.parentEmail = email
            parent.parentPassword = password
            x.parentPassword = password
            parent.save()
            x.save()
            messages.info(request,"Email & Password updated")
            return render(request, 'studentParent/updateinfo.html')

        elif email=='' and location!='None' and contact=='' and password!='' and password==password_repeat:
            x = TemporarySP.objects.get(id=1)
            parent = StudentParent.objects.get(Q(parentName=x.parentName) & Q(parentPassword=x.parentPassword))
            parent.parentLocation = location
            parent.parentPassword = password
            x.parentPassword = password
            parent.save()
            x.save()
            messages.info(request,"Location & Password updated")
            return render(request, 'studentParent/updateinfo.html')

        elif email=='' and location=='None' and contact!='' and password!='' and password==password_repeat:
            x = TemporarySP.objects.get(id=1)
            parent = StudentParent.objects.get(Q(parentName=x.parentName) & Q(parentPassword=x.parentPassword))
            parent.parentContact = contact
            parent.parentPassword = password
            x.parentPassword = password
            parent.save()
            x.save()
            messages.info(request,"Contact & Password updated")
            return render(request, 'studentParent/updateinfo.html')

        elif email != '' and location == 'None' and contact != '' and password == '':
            x = TemporarySP.objects.get(id=1)
            parent = StudentParent.objects.get(Q(parentName=x.parentName) & Q(parentPassword=x.parentPassword))
            parent.parentEmail = email
            parent.parentContact = contact
            parent.save()
            messages.info(request, "Email & Contact updated")
            return render(request, 'studentParent/updateinfo.html')

        elif email != '' and location != 'None' and contact == '' and password == '':
            x = TemporarySP.objects.get(id=1)
            parent = StudentParent.objects.get(Q(parentName=x.parentName) & Q(parentPassword=x.parentPassword))
            parent.parentEmail = email
            parent.parentLocation = location
            parent.save()
            messages.info(request, "Email & Location updated")
            return render(request, 'studentParent/updateinfo.html')

        elif email == '' and location != 'None' and contact != '' and password == '':
            x = TemporarySP.objects.get(id=1)
            parent = StudentParent.objects.get(Q(parentName=x.parentName) & Q(parentPassword=x.parentPassword))
            parent.parentContact = contact
            parent.parentLocation = location
            parent.save()
            messages.info(request, "Location & Contact updated")
            return render(request, 'studentParent/updateinfo.html')

        elif email != '' and location != 'None' and contact != '' and password == '':
            x = TemporarySP.objects.get(id=1)
            parent = StudentParent.objects.get(Q(parentName=x.parentName) & Q(parentPassword=x.parentPassword))
            parent.parentEmail = email
            parent.parentLocation = location
            parent.parentContact = contact
            parent.save()
            messages.info(request, "Email, Location & Contact updated")
            return render(request, 'studentParent/updateinfo.html')

        elif email!='' and location!='None' and contact=='' and password!='' and password==password_repeat:
            x = TemporarySP.objects.get(id=1)
            parent = StudentParent.objects.get(Q(parentName=x.parentName) & Q(parentPassword=x.parentPassword))
            parent.parentEmail = email
            parent.parentLocation = location
            parent.parentPassword = password
            x.parentPassword = password
            parent.save()
            x.save()
            messages.info(request,"Email, Location & Password updated")
            return render(request, 'studentParent/updateinfo.html')

        elif email=='' and location!='None' and contact!='' and password!='' and password==password_repeat:
            x = TemporarySP.objects.get(id=1)
            parent = StudentParent.objects.get(Q(parentName=x.parentName) & Q(parentPassword=x.parentPassword))
            parent.parentLocation = location
            parent.parentContact = contact
            parent.parentPassword = password
            x.parentPassword = password
            parent.save()
            x.save()
            messages.info(request,"Location, Contact & Password updated")
            return render(request, 'studentParent/updateinfo.html')

        elif email!='' and contact!='' and password!='' and password==password_repeat:
            x = TemporarySP.objects.get(id=1)
            parent = StudentParent.objects.get(Q(parentName=x.parentName) & Q(parentPassword=x.parentPassword))
            parent.parentEmail = email
            parent.parentContact = contact
            parent.parentPassword = password
            x.parentPassword = password
            parent.save()
            x.save()
            messages.info(request,"Email, Contact & Password updated")
            return render(request, 'studentParent/updateinfo.html')

        else:
            messages.info(request, "Info not update")
            return render(request, 'studentParent/updateinfo.html')

    else:
        return render(request,'studentParent/updateinfo.html')


def logout(request):

    x = TemporarySP.objects.get(id=1)
    x.delete()

    return render(request,'studentParent/parentlogout.html')


def searchEducator(request):
    if request.method == "POST":
        educatortype = request.POST["educatortype"]
        location = request.POST["location"]

        if educatortype == "Home Educator":
            home_educator = HomeEducator.objects.filter(homeTutorLocation=location)
            context = {'home_educator': home_educator,'type':'Home Educator','location':location,'hname':'Name','hid':'ID','uni':'University','exp':'Experience','hloc':'Location'}
        else:
            outside_educator = OutsideEducator.objects.filter(outsideTutorLocation=location)
            context = {'outside_educator': outside_educator,'type':'Outside Educator','location':location,'oname':'Name','oid':'ID','ins':'Institute','des':'Designation','oloc':'Location'}

        return render(request,"studentParent/educatorsearch.html",context)

    else:
        return render(request, "studentParent/educatorsearch.html")

def showEducatorDetails(request):

    if request.method == "POST":
        educatortype = request.POST["educatortype"]
        id = request.POST["id"]

        if educatortype == "Home Educator":
            home_educator = HomeEducator.objects.get(id=id)
            home_subjects = HomeEducatorSubjects.objects.get(id=id)
            context = {'home_educator': home_educator,'home_subjects':home_subjects,'hname':'Name','hid':'ID','hemail':'Email','uni':'University','dep':'Department','exp':'Experience','hloc':'Location','hcontact':'Contact','hrating':'Rating','hsub':'Subjects'}
        else:
            outside_educator = OutsideEducator.objects.get(id=id)
            outside_subjects = OutsideEducatorSubjects.objects.get(id=id)
            context = {'outside_educator': outside_educator,'outside_subjects':outside_subjects,'oname':'Name','oid':'ID','oemail':'Email','ins':'Institute','des':'Designation','oloc':'Location','ocontact':'Contact','orating':'Rating','osub':'Subjects'}

        return render(request,"studentParent/showdetails.html",context)

    else:
        return render(request, "studentParent/showdetails.html")


