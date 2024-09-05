from django.db import models

# Create your models here.

class Pessoas(models.Model):
    nome = models.CharField(max_length=100)
    matricula = models.IntegerField(max_length=20, unique=True)
    sexo = models.CharField(max_length=1, choices=[('M', 'Masculino'), ('F', 'Femenino'),('O', 'Outros')])
    idade = models.IntegerField()
    ativo = models.CharField(max_length=1, choices=[('S', 'Sim'), ('N', 'Não'),('R', 'Restrição')])
    
    def __str__(self):
        return 
    def __unicode__(self):
        return

class TiposUsuario(models.Model):
    tipo = models.CharField(max_length=1, choices=[('O', 'Operador'), ('G', 'Gestor'),('C', 'Comum')])

    def __str__(self):
        return 

    def __unicode__(self):
        return 

class LocaisLotacoes(models.Model):
    lotacao = models.CharField(max_length=100)
    ativo = models.BooleanField()
    dataCriacao = models.DateField()
    dataFim = models.DateField()
    
    def __str__(self):
        return 

    def __unicode__(self):
        return 

class Usuarios(models.Model):
    usuario = models.ForeignKey("Pessoas", verbose_name=('Usuario'), on_delete=models.CASCADE)
    dataInicio = models.DateField()
    dataFim = models.DateField()
    
    def __str__(self):
        return 

    def __unicode__(self):
        return 

class Lotacoes(models.Model):
    lotação = models.ForeignKey("LocaisLotacoes", verbose_name=("Lotacao"), on_delete=models.CASCADE)
    pessoa = models.ForeignKey("Pessoas", verbose_name=("Pessoa"), on_delete=models.CASCADE)
    dataInicio = models.DateField()
    dataFim = models.DateField()
    
    def __str__(self):
        return 

    def __unicode__(self):
        return 

class TiposContato(models.Model):
    tipoContato = models.CharField(max_length=50)

    def __str__(self):
        return 

    def __unicode__(self):
        return 
class Contatos(models.Model):
    contato = models.CharField(max_length=100)
    tipo = models.ForeignKey("TiposContato", verbose_name=("Tipo"), on_delete=models.CASCADE)

    def __str__(self):
        return 

    def __unicode__(self):
        return 

