from django.shortcuts import render, redirect
from django.http import JsonResponse
from .models import *
from .forms import ContactMesssageForm
import re
from django.contrib import messages
# Create your views here.

def homepage(request):
    bassam_obj = Person.objects.all()[0]
    skills = Skill.objects.filter(person = bassam_obj)
    projects = Project.objects.filter(person_id = bassam_obj.id)
    services = Service.objects.filter(person_id = bassam_obj.id)
    
    if request.method == 'POST':
        form = ContactMesssageForm(request.POST)
        if form.is_valid():
            if not request.POST['name'] or not request.POST['email'] or not request.POST['subject'] or not request.POST['message']:
                return JsonResponse({'success': False, 'message': 'Please fill all the fields.'})
            pat = "^[a-zA-Z0-9-_]+@[a-zA-Z0-9]+\.[a-z]{1,3}$"
            if re.match(pat, form.cleaned_data['email']):
                email = form.cleaned_data['email']
                name = form.cleaned_data['name']
                subject = form.cleaned_data['subject']
                message = form.cleaned_data['message']
                send = ContactMessage.objects.create(email=email, name=name, subject=subject, message=message)
                return JsonResponse({'success': True, 'message': 'Your message has been sent successfully. Please check your email address within the next 24 hours.'})
            else:
                return JsonResponse({'success': False, 'message': 'Please enter a valid email address.'})
        else:
            return JsonResponse({'success': False, 'message': 'Please fill all the fields.'})
    
    context = {
        'bassam' : bassam_obj,
        'skills' : skills,
        'projects' : projects,
        'services' : services,
        'form' : ContactMesssageForm(),
    }
    return render(request, 'index.html', context)

def project_details(request, id):
    project = Project.objects.get(id = id)
    project_images = ProjectImage.objects.filter(project_id = project.id)
    context = {
        'project' : project,
        'project_images' : project_images
    }
    return render(request, 'project-details.html', context)