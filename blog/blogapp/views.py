from django.shortcuts import render, HttpResponse, redirect
from .models import Post, About, Contact
from django.utils import timezone
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages
from django.core.paginator import Paginator

def home(request):
    all_posts = Post.objects.all().order_by('-id')

    if request.user.is_authenticated:
        all_posts = Post.objects.filter(author=request.user).order_by('-id')
        post_count = all_posts.count()
        paginator = Paginator(all_posts, per_page=6)
        page_number = request.GET.get('page')
        final_posts = paginator.get_page(page_number)
        return render(request, 'blog-detail.html', {'all_posts': final_posts} )

    paginator = Paginator(all_posts, per_page=6)
    page_number = request.GET.get('page')
    final_posts = paginator.get_page(page_number)


    return render (request, 'index.html', {'all_posts':final_posts})

def about(request):
    abt_data = About.objects.last()
    return render(request, 'about.html', {"abt_data":abt_data})

def contact(request):

    if request.method == "POST":
        name = request.POST['cont_name']
        email = request.POST['cont_email']
        phone = request.POST['cont_phone']
        message = request.POST['cont_message']

        cont_obj = Contact(name=name, email=email, phone=phone, message=message)
        cont_obj.save()
        
    return render(request, 'contact.html')

def post(request):
    all_posts = Post.objects.filter(author=request.user)
    return render(request, 'post.html')

def post_details(request, pk):
    post_detail = Post.objects.get(id=pk)
    return render(request, 'post_details.html', {"post_detail": post_detail})

def post_schedulr(request):
    return render(request, 'schedul.html')

def post_uploader(request):

    if request.method == 'POST':
        author = request.user
        post_title = request.POST['post']
        post_text = request.POST['content']
        post_created_date = request.POST['created']
        post_published_date = request.POST['publish']

        # print(author, post_title, post_text,  post_created_date, post_published_date)
        up_obj = Post(author=author, title=post_title, text=post_text, created_date=post_created_date ,published_date=post_published_date)
        up_obj.save()
    # print('success')
    return render(request, 'uploader.html')

def profile(request):
    post_count = Post.objects.filter(author=request.user).count()
    return render(request, 'profile.html', {'post_count': post_count})

def edit_profile(request):
    usr_data = User.objects.get(username=request.user)

    if request.method=="POST":
        usr_data.first_name = request.POST['first_name']
        usr_data.last_name = request.POST['last_name']
        # usr_data.email = request.POST['']
        try:
            usr_data.save()
            return redirect('profile')
        except KeyError:
            messages.error(request, KeyError)
    return render(request, 'profile_edit.html', {'usr_data' : usr_data})

def edit_post(request, pk):
    post = Post.objects.get(id=pk)

    if request.method == 'POST':
        post.title = request.POST['post']
        post.text = request.POST['content']
        # post.creaated_on = request.POST['created']
        # post.published_on = request.POST['publish']
        try:
            post.save()
            return redirect('home')
        except KeyError:
            messages.error(request, KeyError)

    return render(request, 'edit-post.html', {'post' : post})

def delete_post(request, pk):
    del_post = Post.objects.get(id=pk)
    del_post.delete()
    return redirect('home')

def register(request):

    if request.method == 'POST':
        user_name = request.POST.get('user_name')
        user_email = request.POST.get('user_email')
        first_name = request.POST.get('first_name')
        last_name = request.POST.get('last_name')
        user_password = request.POST.get('user_password')
        user_conf_password = request.POST.get('user_conf_password')

        if user_password != user_conf_password:
            messages.error(request, 'Password is not matching...')
            return redirect('register')
        # elif len(user_name) > 3 :
        #     messages.error(request,'Username should not more than 8 characters...')
        #     return redirect('register')
        else:
            user = User.objects.create_user(user_name, user_email, user_password)
            user.first_name = first_name
            user.last_name = last_name
            user.save()
            messages.error(request, 'Successfully registered')
            return redirect('login')

    return render(request, 'register.html')


def usrLogin(request):

    if request.method == 'POST':
        user_name = request.POST.get('user_name')
        user_password = request.POST.get('user_password')

        user_auth = authenticate(username=user_name, password=user_password)
        print(user_auth)
        if user_auth is not None:
            login(request, user_auth)
            messages.success(request, 'Successfully Logged in')
            return redirect('home')
        else:
            # messages.error(request, 'There is no user check your username or password')
            return redirect('login')

    return render(request, "login.html")


def usrLogout(request):
    logout(request)
    return redirect('home')