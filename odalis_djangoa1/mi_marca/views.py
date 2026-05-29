from django.shortcuts import render

def inicio(request):
    contexto = {
        "nombre": "Colon Vargas",
        "titulo": "Portafolio Profesional de Colon Vargas",
        "descripcion": "Estudiante enfocado en desarrollo de software, diseño web e inteligencia artificial.",
        "habilidades": [
            "Python",
            "Django",
            "HTML",
            "CSS",
            "JavaScript",
            "Bases de datos",
            "Inteligencia Artificial",
            "Diseño web"
        ],
        "proyectos": [
            {
                "nombre": "Landing Page Personal",
                "detalle": "Página web creada para presentar mi marca personal e información profesional."
            },
            {
                "nombre": "Sistema Web Educativo",
                "detalle": "Proyecto orientado al aprendizaje mediante herramientas digitales."
            },
            {
                "nombre": "Asistente con IA",
                "detalle": "Idea de asistente inteligente para apoyar tareas académicas y tecnológicas."
            }
        ]
    }
    return render(request, "mi_marca/index.html", contexto)
