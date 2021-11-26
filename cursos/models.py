from django.db import models

# Create your models here.

class Curso:
    id: int
    curso_nombre: str
    curso_imagen: str
    curso_descripcion: str
    curso_precio: str
    curso_vigencia: int
    curso_enlace_externo: str
