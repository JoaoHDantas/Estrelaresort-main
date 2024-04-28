from django.http import HttpResponse
from django.shortcuts import render
from django.contrib.auth.models import User
from django.contrib.auth import authenticate
from django.contrib.auth import login as login_django
from django.contrib.auth.decorators import login_required

# Create your views here.
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
            return HttpResponse("autenticado")
        else:
            return HttpResponse('email ou senha errada')

@login_required(login_url="/auth/login/")
def index(request):
    if request.user.is_authenticated:
        return HttpResponse('TA LOGADO NA PAGINA')
    return HttpResponse ('voce nao esta logado')