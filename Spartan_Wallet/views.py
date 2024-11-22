from django.shortcuts import render

def Login(request):

    contexto = { str(request) }
    return render(request, 'Login.html', {'range': range(5)})