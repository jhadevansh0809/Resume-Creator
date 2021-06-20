from django.shortcuts import render

# Create your views here.
from .models import Resume
import pdfkit
from django.http import HttpResponse
from django.template import context, loader
import io


def index(request):
    Resume.objects.all().delete()
    if request.method=='POST':
        name=request.POST.get("name","")
        description=request.POST.get("description","")
        address=request.POST.get("address","")
        phone=request.POST.get("phone","")
        email=request.POST.get("email","")
        degree=request.POST.get("degree","")
        skills=request.POST.get("skills","")
        university=request.POST.get("university","")
        university_score=request.POST.get("university_score","")
        twelveth_schooling=request.POST.get("twelveth_schooling","")
        twelveth_score=request.POST.get("twelveth_score","")
        tenth_schooling=request.POST.get("tenth_schooling","")
        tenth_score=request.POST.get("tenth_score","")
        experience=request.POST.get("experience","")
        projects=request.POST.get("projects","")
        languages=request.POST.get("languages","")
        awards=request.POST.get("awards","")

        res=Resume(name=name,description=description,address=address,phone=phone,email=email,degree=degree,skills=skills,university=university,university_score=university_score,twelveth_schooling=twelveth_schooling,twelveth_score=twelveth_score,tenth_schooling=tenth_schooling,tenth_score=tenth_score,experience=experience,projects=projects,languages=languages,awards=awards)
        res.save()
        user_resume = Resume.objects.filter(name=str(res.name)).first()
        template = loader.get_template('resume/dwnld.html')
        html = template.render({'user_resume':user_resume})
        options ={
        'page-size':'Letter',
        'encoding':"UTF-8",
        }
        pdf = pdfkit.from_string(html,False,options)
        response = HttpResponse(pdf,content_type='application/pdf')
        response['Content-Disposition'] ='attachment'
        filename = "resume.pdf"
        return response
        

    return render(request,'resume/index.html')