from django.db import models

class Psicologo(models.Model):
    nome = models.CharField(max_length=100)
    especializacao = models.CharField(max_length=100)
    formacao = models.TextField()
    foto = models.ImageField(upload_to='psicologos/')
    email = models.EmailField()
    telefone = models.CharField(max_length=20)
    
    def __str__(self):
        return self.nome

class Agendamento(models.Model):
    psicologo = models.ForeignKey(Psicologo, on_delete=models.CASCADE)
    cliente_nome = models.CharField(max_length=100)
    data = models.DateTimeField()
    idade = models.IntegerField()
    descricao = models.TextField()

    def __str__(self):
        return f"Agendamento com {self.psicologo.nome} em {self.data}"

class Instituicao(models.Model):
    nome = models.CharField(max_length=255)
    endereco = models.CharField(max_length=255)

    def __str__(self):
        return self.nome