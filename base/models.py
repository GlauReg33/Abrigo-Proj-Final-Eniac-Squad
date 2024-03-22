from django.db import models

# Create your models here.
class CadastroAdotantes(models.Model):
    nome = models.CharField(max_length=50)
    email = models.EmailField(max_length=75)
    telefone = models.CharField(max_length=20)
    senha= models.CharField(max_length=50)
    Cidade = models.CharField(max_length=40)
    Rua = models.CharField(max_length=20)
    Bairro = models.CharField(max_length=30)
    # tipo_do_Animal = models.CharField(max_length=20)
    # pesquisar como inserir select cao ou gato no 
    # formulário e como registrar isso na model
    # cep = models.CharField(('CEP')),
    data_Adocao = models.DateTimeField(auto_now_add=True)
    
    
    #def _str(self):
    #    return f 'self.nome [{self.email}]'
    class Meta:
        verbose_name = 'Formulario de Adotante'
        verbose_name_plural = 'Formularios de Adotantes'
        ordering = ['-data_Adocao']