from django.shortcuts import render, redirect
from django.contrib import messages
from django.contrib.auth.models import User, auth
from posts.models import Post
from posts.forms import ImageForm
# Create your views here.
def frontpage(request):
    posts=Post.objects.all()
    return render(request,'frontpage.html',{'posts':posts})



def create(request):
    if request.method == 'POST':
        form = ImageForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            # Get the current instance object to display in the template
            img_obj = form.instance
            return render(request, 'create.html', {'form': form, 'img_obj': img_obj})
    else:
        form = ImageForm()
    return render(request, 'create.html', {'form': form})

def login(request):
    if request.method== 'POST':
        username = request.POST['username']
        password = request.POST['password']

        user = auth.authenticate(username=username,password=password)

        if user is not None:
            auth.login(request, user)
            return redirect("create")
        else:
            messages.info(request,'invalid credentials')
            return redirect('login')

    else:
        return render(request,'login.html')

def register(request):

    if request.method == 'POST':
        first_name = request.POST['first_name']
        last_name = request.POST['last_name']
        username = request.POST['username']
        password1 = request.POST['password1']
        password2 = request.POST['password2']
        email = request.POST['email']

        if password1==password2:
            if User.objects.filter(username=username).exists():
                messages.info(request,'Username Taken')
                return redirect('register')
            elif User.objects.filter(email=email).exists():
                messages.info(request,'Email Taken')
                return redirect('register')
            else:
                user = User.objects.create_user(username=username, password=password1, email=email,first_name=first_name,last_name=last_name)
                user.save();
                print('user created')
                return redirect('login')

        else:
            messages.info(request,'password not matching..')
            return redirect('register')

    else:
        return render(request,'register.html')



def logout(request):
    auth.logout(request)
    return redirect('/')
