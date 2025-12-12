from django.db import models

class Estudante(models.Model):
    nome = models.CharField(max_length=100)
    email = models.EmailField(blank=False, max_length=100, unique=True)
    cpf = models.CharField(max_length=11, unique=True)
    data_nascimento = models.DateField()
    celular = models.CharField(max_length=14)

    def __str__(self):
        return self.nome
    

    class Curso(models.Model):
        NIVEL = (
            ("B", "Básico"),
            ("I", "Intermediário"),
            ("A", "Avançado"),
        )
        codigo = models.CharField(max_length=10, unique=True)
        descricao = models.CharField(max_length=200)
        nivel = models.CharField(
            max_length=1, choices=NIVEL, blank=False, null=False, default="B"
        )

        def __str__(self):
            return self.nome