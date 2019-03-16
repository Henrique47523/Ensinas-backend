from django.shortcuts import render
from app.models import Materia, Mentor
from app import forms

def auth_cadastro(request):
    return render(request, 'auth_cadastro.html')

def auth_login(request):
    form_estudante = forms.EstudanteLoginForm()
    form_mentor = forms.MentorLoginForm()

    return render(request, 'auth_login.html', {
            'form_estudante': form_estudante,
            'form_mentor': form_mentor
    })

def estudante_home(request):
    materias = Materia.objects.all()
    mentores = Mentor.objects.filter(aprovado=True)

    return render(request, 'estudante_home.html', {
        "materias": materias,
        "mentores": mentores
        })


def estudante_materia(request, id_materia):
    materias = Materia.objects.all()
    materia_atual = Materia.objects.get(pk=id_materia)
    mentores = Mentor.objects.filter(materia=id_materia,aprovado=True)

    return render(request, 'estudante_home.html', {
        "materias": materias, 
        "materia_atual": materia_atual,
        "mentores": mentores
        })

def mentor_home(request):
    return render(request, 'mentor_home.html')