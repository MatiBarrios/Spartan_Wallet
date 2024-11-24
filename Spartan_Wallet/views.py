from django.shortcuts import render

from django.contrib.auth import authenticate, login as login_django

def Login(request):

    #contexto = { str(request) }

    username = request.POST.get("username",default=None)
    password = request.POST.get("password",default=None)
    print(username)
    print(password)
    usuario = authenticate(request, username = username, password = password)
    print(usuario)

        #hacer el login en caso de que el usuario se haya autenticado
    if usuario:
        login_django(request, usuario)
        
    return render(request, 'Login.html', {})