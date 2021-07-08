from django.conf import settings
from django.db import models
from django.utils import timezone

#définir notre modèle (qui est un object): models.Model signifie que Post est un modèle Django. Comme ça, Django sait qu'il doit l'enregistrer dans la base de données
class Post(models.Model): #Post: le nom du modèle
  # definir les proprietés(author, title, text....)
    author = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE) #ForeignKey: un lien vers un autre modèle
    title = models.CharField(max_length=200) #CharField: permet de définir un champ texte avec un nombre limité de caractères
    text = models.TextField() #TextField: définit 1 champ text sans limite de caractères.Parfait pour le contenu d'1 blog post, non ?
    created_date = models.DateTimeField(default=timezone.now)#DateTimeField: définit que le champ en question est une date ou une heure.
    published_date = models.DateTimeField(blank=True, null=True)
    
    # méthode publish()
    def publish(self):
        self.published_date = timezone.now()
        self.save()

    def __str__(self):
        return self.title #renvoie du texte avec un titre de Post


