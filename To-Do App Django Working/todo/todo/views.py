from django.shortcuts import render, redirect
from django.contrib.auth.models import User
from todo import models
from todo.models import TODOO
from django.contrib.auth import login
from django.contrib.auth import authenticate, login,logout

from django.contrib import messages  # For showing messages to users


def signup(request):
    if request.method=='POST':
        fnm = request.POST.get('fnm')
        emailid = request.POST.get('email')
        pwd = request.POST.get('pwd')
        print(fnm,emailid,pwd)


         # Check if the username or email already exists
        if User.objects.filter(username=fnm).exists():
            messages.warning(request, "Username already exists.")
            print("Username already exists")
            return redirect('login')
        if User.objects.filter(email=emailid).exists():
            messages.warning(request, "Email already exists.")
            print("email already exists")
            return redirect('login')
        

        my_user= User.objects.create_user(fnm,emailid,pwd)
        my_user.save()
        return redirect('login')

    return render(request,'signup.html')

def login_view(request):
    if request.method=='POST':
        fnm = request.POST.get('fnm')
        pwd = request.POST.get('pwd')
        print(fnm,pwd)
        userr= authenticate(request, username = fnm,password = pwd)
        if userr is not None:
            login(request,userr)
            return redirect('/todopage')
        else:
            return redirect('/login')
    

    return render(request, 'loginn.html')

def todo(request):
    if request.method=='POST':
        title = request.POST.get('title')
        print(title)

        description = request.POST.get('description')
        print(description)
        
        due_date = request.POST.get('due_date')
        print(due_date)

        tag = request.POST.get('tags')
        print(tag)

        status = request.POST.get('status')
        print(status)

        # Add basic validation (e.g., checking for empty fields)
        if not title or not description or not status:
            messages.error(request, "All fields except Due Date and Tag are required.")
            return redirect('/todopage')
        


        # Create the new task
        obj = models.TODOO(title=title, status=status, description=description, due_date=due_date, tag=tag, user=request.user)
        obj.save()

        # Fetch the updated list of todos for the user
        res = models.TODOO.objects.filter(user=request.user).order_by('-date')
        return redirect('/todopage', {'res': res})
    
    res=models.TODOO.objects.filter(user=request.user).order_by('-date')
    return render(request, 'todo.html',{'res':res})



def edit_todo(request,srno):
    if request.method=='POST':
        title = request.POST.get('title')
        print(title)
        description = request.POST.get('description')
        print(description)
        deu_date = request.POST.get('deu_date')
        print(deu_date)
        tag = request.POST.get('tag')
        print(tag)
        status = request.POST.get('status')
        print(status)

         # Add basic validation (e.g., checking for empty fields)
        if not title or not description or not status:
            messages.error(request, "All fields except Due Date and Tag are required.")
            return redirect(f'/edit_todo/{srno}')
        

        obj=models.TODOO.objects.get(srno=srno)
        obj.title=title
        obj.description=description
        obj.deu_date=deu_date
        obj.status=status
        obj.tag=tag
        obj.save()
        user=request.user
        
        return redirect('/todopage')
    obj=models.TODOO.objects.get(srno=srno)
    return render(request, 'edit_todo.html', {'obj':obj})

def delete_todo(request,srno):
    obj=models.TODOO.objects.get(srno=srno)
    obj.delete()
    return redirect('/todopage')

def signout(request):
    logout(request)
    return redirect('/login')