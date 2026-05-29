from django.shortcuts import render
from django.shortcuts import render

def inicio(request):
    datos = {
        "nombre": "Odalis",
        "marca": "ODALIS | Perfil Digital",
        "descripcion": "Estudiante interesada en el desarrollo web, la innovación tecnológica y el aprendizaje continuo.",
        "habilidades": [
            "Python",
            "Django",
            "HTML5",
            "CSS3",
            "JavaScript",
            "Diseño Web"
        ],
        "proyectos": [
            "Perfil digital interactivo",
            "Aplicación web académica",
            "Sistema de gestión de información"
        ]
    }

    return render(request, 'mi_marca/index.html', datos)
def principal(request):
    return render(request, "principal/index.html")
