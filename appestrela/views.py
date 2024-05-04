from django.http import HttpResponse
from django.shortcuts import render
from django.contrib.auth.models import User
from django.contrib.auth import authenticate
from django.contrib.auth import login as login_django
from django.contrib.auth.decorators import login_required
from .models import Post
# Create your views here.


def post_list(request):
    posts = Post.objects.all()
    return render(request, 'posts/post_list.html', {'posts': posts})



def carousel(request):
    posts = Post.objects.all()
    return render(request, 'posts/carousel.html', {'posts': posts})

def post_detail(request, pk):
    post = Post.objects.get(pk=pk)
    return render(request, 'posts/post_detail.html', {'post': post})

def cadastro(request):
    if request.method == "GET":
        return render(request, 'cadastro.html')
    else:
        username = request.POST.get('username')
        email = request.POST.get('email')
        senha = request.POST.get('senha')

        user = User.objects.filter(username=username).first()

        if user:
            return HttpResponse('ja existe alguem com esse nome')
        
        user = User.objects.create_user(username=username, email=email, password=senha)
        user.save()
        
        return HttpResponse("usuario cadastrado")

def login(request):
    if request.method == "GET":
        return render(request, 'login.html')
    else:
        username = request.POST.get('username')
        senha = request.POST.get('senha')

        user = authenticate(username=username, password=senha)

        if user:
            login_django(request, user)
            return render(request, 'index.html')
        else:
            return HttpResponse('Email ou Senha errada, tente novamente')

@login_required(login_url="/auth/login/")
def index(request):
    if request.user.is_authenticated:
        posts = Post.objects.all()
        return render(request, 'index.html', {'posts': posts})
    else:
        return HttpResponse ('Você não está logado, volte e faça do login ou cadastro')