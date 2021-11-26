from django.shortcuts import render

from .models import Curso

# Create your views here.
def index(request):

    curso_ergonomia = Curso()
    curso_accidentes_de_trabajo = Curso()
    curso_sismos = Curso()
    curso_identificacion_peligros_riesgos = Curso()

    curso_ergonomia.curso_nombre = 'Ergonomía'
    curso_ergonomia.curso_imagen = 'curso_ergonomia.jpg'
    curso_ergonomia.curso_descripcion = 'Incluye examen'
    curso_ergonomia.curso_precio = 'Gratuito'
    curso_ergonomia.curso_vigencia = 1
    curso_ergonomia.curso_enlace_externo = 'https://docs.google.com/presentation/d/1SYfBLXRC_4PqkGBThGUBkfeau824AUfO/edit?usp=sharing&ouid=100483376780757384486&rtpof=true&sd=true'

    curso_accidentes_de_trabajo.curso_nombre = 'Accidentes de Trabajo'
    curso_accidentes_de_trabajo.curso_imagen = 'curso_accidentes.jpg'
    curso_accidentes_de_trabajo.curso_descripcion = 'Incluye examen'
    curso_accidentes_de_trabajo.curso_precio = 'Gratuito'
    curso_accidentes_de_trabajo.curso_vigencia = 1
    curso_accidentes_de_trabajo.curso_enlace_externo = 'https://docs.google.com/presentation/d/1AePBLx1Rh-rhcG-ibVktmSLLGK7lp0zP/edit?usp=sharing&ouid=100483376780757384486&rtpof=true&sd=true'

    curso_sismos.curso_nombre = 'Sismos'
    curso_sismos.curso_imagen = 'curso_sismos.jpg'
    curso_sismos.curso_descripcion = 'Incluye examen'
    curso_sismos.curso_precio = 'Gratuito'
    curso_sismos.curso_vigencia = 1
    curso_sismos.curso_enlace_externo = 'https://docs.google.com/presentation/d/1OfyAfGX6TdAXtruBjEzFEHnLkMS-_m7M/edit?usp=sharing&ouid=100483376780757384486&rtpof=true&sd=true'


    curso_identificacion_peligros_riesgos.curso_nombre = 'Identificación de Peligros y Riesgos'
    curso_identificacion_peligros_riesgos.curso_imagen = 'curso_identificacion_peligros.jpg'
    curso_identificacion_peligros_riesgos.curso_descripcion = 'Incluye examen'
    curso_identificacion_peligros_riesgos.curso_precio = 'Gratuito'
    curso_identificacion_peligros_riesgos.curso_vigencia = 0
    curso_identificacion_peligros_riesgos.curso_enlace_externo = 'https://docs.google.com/presentation/d/1GmjrJhMBMCO-SfJfX6BwZmGhAgQlwIex/edit?usp=sharing&ouid=100483376780757384486&rtpof=true&sd=true'

    cursos = [curso_ergonomia, curso_accidentes_de_trabajo, curso_sismos, curso_identificacion_peligros_riesgos]

    return render(request, 'index.html', {'cursos': cursos})
