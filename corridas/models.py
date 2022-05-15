from django.db import models

class Corrida(models.Model):
    circuito = models.CharField(max_length=80)
    categoria= models.CharField(max_length=30)

    def __str__(self):
        return f'{self.circuito} ({self.categoria})'

class Equipa(models.Model):

    inscricao = models.ForeignKey(
        Corrida,
        on_delete=models.CASCADE,
        related_name = 'participações'
        )

    def __str__(self):
        return f'({self.inscricao})'

class Veiculo(models.Model):
     tipo = models.CharField(max_length=30)
     cilindrada = models.IntegerField()
     equipa = models.ManyToManyField(Equipa)

     def __str__(self):
         return f'{self.tipo} ({self.cilindrada})'

class Piloto(models.Model):
    nome = models.CharField(max_length=100)
    idade = models.IntegerField()

    def __str__(self):
        return f'{self.nome} ({self.idade})'