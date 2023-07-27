from django.shortcuts import render,redirect
from studentParent.models import StudentParent,TemporarySP
from educator.models import HomeEducator,OutsideEducator,HomeEducatorSubjects,OutsideEducatorSubjects,TemporaryE
from .models import Request,Deals,feedback
from django.contrib import messages
from django.db.models import Q



def homePage(request):
    return render(request,'home/home.html')


def aboutus(request):
    return render(request,'home/aboutus.html')

def subject(request):
    return render(request,'home/subjects.html')

def books(request):
    return render(request,'home/books.html')

def worksheet(request):
    return render(request,'home/worksheet.html')

def feedpage(request):
    if request.method=='POST':
        name=request.POST['name']   
        surname=request.POST['surname']
        email=request.POST['email']
        comment=request.POST['comment']
        feedback(Name=name,Surname=surname,Email=email,Comment=comment).save()
        messages.success(request,'The New Feedback '+request.POST['name']+" is saved Successfully...!")
        return render(request,'home/feedback.html')
    else:
        return render(request,'home/feedback.html')






def confirmRequest(request):
    if request.method == "POST":
        educatortype = request.POST["educatortype"]
        educatorid = request.POST["educatorid"]

        if educatortype == "Home Educator":
            if HomeEducator.objects.filter(id=educatorid).exists():

                x = TemporarySP.objects.get(id=1)
                parent = StudentParent.objects.get(Q(parentName=x.parentName) & Q(parentPassword=x.parentPassword))

                y = HomeEducator.objects.get(id=educatorid)

                req = Request(educatorType=educatortype,educatorId=educatorid,educatorName=y.homeTutorName,
                              parentId=parent.id,parentName=parent.parentName)

                req.save()
                messages.info(request, "Request Sent")
                return redirect("confirmrequest")

            else:
                messages.info(request,"Invalid Educator Id")

        else:
            if OutsideEducator.objects.filter(id=educatorid).exists():

                x = TemporarySP.objects.get(id=1)
                parent = StudentParent.objects.get(Q(parentName=x.parentName) & Q(parentPassword=x.parentPassword))

                y = OutsideEducator.objects.get(id=educatorid)

                req = Request(educatorType=educatortype, educatorId=educatorid, educatorName=y.outsideTutorName,
                              parentId=parent.id, parentName=parent.parentName)

                req.save()
                messages.info(request, "Request Sent")
                return redirect("confirmrequest")

            else:
                messages.info(request, "Invalid Educator Id")

    return render(request, "home/confirmrequest.html")


def showRequest(request):

    y = TemporaryE.objects.get(id=1)

    if request.method == "GET":

        if y.tutorType == "Home Educator":

            educator = HomeEducator.objects.get(Q(homeTutorName=y.tutorName) & Q(homeTutorPassword=y.tutorPassword))

            req = Request.objects.filter(educatorId=educator.id)
            context = {"req":req}
            return render(request, 'home/showrequest.html', context)

        else:
            educator = OutsideEducator.objects.get(Q(outsideTutorName=y.tutorName) & Q(outsideTutorPassword=y.tutorPassword))

            req = Request.objects.filter(educatorId=educator.id)
            context = {"req": req}
            return render(request, 'home/showrequest.html', context)

    else:
        parentid = request.POST["parentid"]

        if parentid == "":
            messages.info(request,"Invalid Parent ID")
            return redirect('showrequest')

        if y.tutorType == "Home Educator":

            educator = HomeEducator.objects.get(Q(homeTutorName=y.tutorName) & Q(homeTutorPassword=y.tutorPassword))

            if StudentParent.objects.filter(id=parentid).exists():

                if Request.objects.filter(Q(parentId=parentid) & Q(educatorId=educator.id)).exists():

                    req = Request.objects.get(Q(parentId=parentid) & Q(educatorId=educator.id))

                    deal = Deals(educatorType=req.educatorType, educatorId=req.educatorId, educatorName=req.educatorName,
                                  parentId=req.parentId, parentName=req.parentName)

                    deal.save()
                    req.delete()
                    messages.info(request, "Request accepted")
                else:
                    messages.info(request, "No such request")
            else:
                messages.info(request,"Invalid Parent Id")

        else:

            educator = OutsideEducator.objects.get(Q(outsideTutorName=y.tutorName) & Q(outsideTutorPassword=y.tutorPassword))

            if StudentParent.objects.filter(id=parentid).exists():

                if Request.objects.filter(Q(parentId=parentid) & Q(educatorId=educator.id)).exists():

                    req = Request.objects.get(Q(parentId=parentid) & Q(educatorId=educator.id))

                    deal = Deals(educatorType=req.educatorType, educatorId=req.educatorId,educatorName=req.educatorName,
                                 parentId=req.parentId, parentName=req.parentName)

                    deal.save()
                    req.delete()
                    messages.info(request, "Request accepted")
                else:
                    messages.info(request, "No such request")
            else:
                messages.info(request, "Invalid Parent Id")

        if y.tutorType == "Home Educator":

            educator = HomeEducator.objects.get(Q(homeTutorName=y.tutorName) & Q(homeTutorPassword=y.tutorPassword))

            req = Request.objects.filter(educatorId=educator.id)
            context = {"req":req}
            return render(request, 'home/showrequest.html', context)

        else:
            educator = OutsideEducator.objects.get(Q(outsideTutorName=y.tutorName) & Q(outsideTutorPassword=y.tutorPassword))

            req = Request.objects.filter(educatorId=educator.id)
            context = {"req": req}
            return render(request, 'home/showrequest.html', context)



