from django.db import models

class Alumno(models.Model):
    nombre = models.CharField(max_length=100)
    grupo = models.CharField(max_length=10)
    matricula = models.CharField(max_length=20, unique=True)

    def __str__(self):
        return f"{self.nombre} ({self.matricula})"

class Solicitud(models.Model):
    TIPOS_CANALIZACION = [
        ('Becas', 'Becas'),
        ('Asesorías', 'Asesorías'),
        ('Psicológica', 'Atención Psicológica'),
    ]

    alumno = models.ForeignKey(Alumno, on_delete=models.CASCADE)
    tipo = models.CharField(max_length=20, choices=TIPOS_CANALIZACION)
    descripcion = models.TextField()
    fecha_creacion = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.tipo} - {self.alumno.nombre}"
