from django.shortcuts import render

from .models import Curso

# Create your views here.
def index(request):

    curso_ergonomia = Curso()
    curso_accidentes_de_trabajo = Curso()
    curso_sismos = Curso()
    curso_identificacion_peligros_riesgos = Curso()
    curso_lavado_activos = Curso()
    curso_lavado_activos_2023 = Curso()

    curso_ergonomia.curso_nombre = 'Ergonomía'
    curso_ergonomia.curso_imagen = 'curso_ergonomia.jpg'
    curso_ergonomia.curso_descripcion = 'Incluye examen'
    curso_ergonomia.curso_precio = 'Gratuito'
    curso_ergonomia.curso_vigencia = 0
    curso_ergonomia.curso_enlace_externo = 'https://docs.google.com/presentation/d/1SYfBLXRC_4PqkGBThGUBkfeau824AUfO/edit?usp=sharing&ouid=100483376780757384486&rtpof=true&sd=true'
    curso_ergonomia.curso_enlace_evaluacion = '#'

    curso_accidentes_de_trabajo.curso_nombre = 'Accidentes de Trabajo'
    curso_accidentes_de_trabajo.curso_imagen = 'curso_accidentes.jpg'
    curso_accidentes_de_trabajo.curso_descripcion = 'Incluye examen'
    curso_accidentes_de_trabajo.curso_precio = 'Gratuito'
    curso_accidentes_de_trabajo.curso_vigencia = 0
    curso_accidentes_de_trabajo.curso_enlace_externo = 'https://docs.google.com/presentation/d/1AePBLx1Rh-rhcG-ibVktmSLLGK7lp0zP/edit?usp=sharing&ouid=100483376780757384486&rtpof=true&sd=true'
    curso_accidentes_de_trabajo.curso_enlace_evaluacion = '#'

    curso_sismos.curso_nombre = 'Sismos'
    curso_sismos.curso_imagen = 'curso_sismos.jpg'
    curso_sismos.curso_descripcion = 'Incluye examen'
    curso_sismos.curso_precio = 'Gratuito'
    curso_sismos.curso_vigencia = 0
    curso_sismos.curso_enlace_externo = 'https://docs.google.com/presentation/d/1OfyAfGX6TdAXtruBjEzFEHnLkMS-_m7M/edit?usp=sharing&ouid=100483376780757384486&rtpof=true&sd=true'
    curso_sismos.curso_enlace_evaluacion = '#'

    curso_identificacion_peligros_riesgos.curso_nombre = 'Identificación de Peligros y Riesgos'
    curso_identificacion_peligros_riesgos.curso_imagen = 'curso_identificacion_peligros.jpg'
    curso_identificacion_peligros_riesgos.curso_descripcion = 'Incluye examen'
    curso_identificacion_peligros_riesgos.curso_precio = 'Gratuito'
    curso_identificacion_peligros_riesgos.curso_vigencia = 0
    curso_identificacion_peligros_riesgos.curso_enlace_externo = 'https://docs.google.com/presentation/d/1GmjrJhMBMCO-SfJfX6BwZmGhAgQlwIex/edit?usp=sharing&ouid=100483376780757384486&rtpof=true&sd=true'
    curso_identificacion_peligros_riesgos.curso_enlace_evaluacion = '#'

    curso_lavado_activos.curso_nombre = 'Lavado de Activos (2022)'
    curso_lavado_activos.curso_imagen = 'curso_lavado_activos.jpg'
    curso_lavado_activos.curso_descripcion = 'Incluye examen'
    curso_lavado_activos.curso_precio = 'Gratuito'
    curso_lavado_activos.curso_vigencia = 0
    curso_lavado_activos.curso_enlace_externo = 'https://drive.google.com/file/d/1DmzgMyYsugZyKf_y9yvm3HNSCGYLaq-T/view?usp=sharing'
    curso_lavado_activos.curso_enlace_evaluacion = 'https://forms.office.com/Pages/ResponsePage.aspx?id=DQSIkWdsW0yxEjajBLZtrQAAAAAAAAAAAAFhEIRB5oVURjAxVFBMSTVFTjFHT01ISlRBTUdENFNSRi4u'
    
    curso_lavado_activos_2023.curso_nombre = 'Lavado de Activos (Diciembre 2023)'
    curso_lavado_activos_2023.curso_imagen = 'curso_lavado_activos_2023.jpg'
    curso_lavado_activos_2023.curso_descripcion = 'Incluye examen'
    curso_lavado_activos_2023.curso_precio = 'Gratuito'
    curso_lavado_activos_2023.curso_vigencia = 1
    curso_lavado_activos_2023.curso_enlace_externo = 'https://docs.google.com/presentation/d/1KiSuNXz3SQMTXO0jDsnqqESV7SSwc0iH/edit?usp=sharing&ouid=100483376780757384486&rtpof=true&sd=true'
    curso_lavado_activos_2023.curso_enlace_evaluacion = 'https://forms.office.com/Pages/DesignPageV2.aspx?origin=NeoPortalPage&subpage=design&id=DQSIkWdsW0yxEjajBLZtrQAAAAAAAAAAAAFhEIRB5oVUQVVGWTdJS0M1RUZYWUJMUTQ0WUtTRE9SWi4u&preview=%257B%2522ViewModeIndex%2522%3A1%257D'

    cursos = [curso_lavado_activos_2023, curso_lavado_activos, curso_ergonomia, curso_accidentes_de_trabajo, curso_sismos, curso_identificacion_peligros_riesgos]

    return render(request, 'index.html', {'cursos': cursos})
