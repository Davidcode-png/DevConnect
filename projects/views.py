from turtle import right
from django.shortcuts import render,HttpResponse,redirect
from .models import Project,Tag
from django.contrib.auth.decorators import login_required
from .forms import ProjectForm
from users.models import Profile
from .utils import searchProjects,paginationProject

def projects(request):
    projects, text = searchProjects(request)
    custom_range, projects = paginationProject(request,projects, 6) 
    #profile = Profile.objects.all()
    
    context = {'projects':projects,'text':text,'custom_range':custom_range}
    return render(request,'projects/project.html',context)

def project(request,pk):
    projectObj = Project.objects.get(id=pk)
    tags = projectObj.tags.all()
    context = {'project':projectObj,'tags':tags}
    return render(request,'projects/single-project.html',context)

@login_required(login_url="login")
def createProject(request):
    profile = request.user.profile
    form = ProjectForm()

    if request.method == 'POST':
        form = ProjectForm(request.POST,request.FILES)
        if form.is_valid():
            project = form.save(commit=False)
            project.owner = profile
            project.save()
            return redirect(projects)
        else:
            print(form.errors)
    context = {'form':form}
    return render(request,"projects/project-form.html",context)

@login_required(login_url="login")
def updateProject(request,pk):
    profile = request.user.profile
    project = profile.project_set.get(id=pk)
    form = ProjectForm(instance=project)

    if request.method == 'POST':
        form = ProjectForm(request.POST,request.FILES,instance=project)
        if form.is_valid():
            form.save()
            return redirect(projects)
        else:
            print(form.errors)
    context = {'form':form}
    return render(request,"projects/project-form.html",context)

@login_required(login_url="login")
def deleteProject(request,pk):
    profile = request.user.profile
    project = profile.project_set.get(id=pk)
    if request.method == 'POST':
        project.delete()
        return redirect(projects)
    context = {'object':project}
    return render(request,"delete_confirmation.html",context)