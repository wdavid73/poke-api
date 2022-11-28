from django.db import models
from poke_api.Type.Model.ModelType import Type

def nameFile(instace, filename):
  return '/'.join(['images','pokemon', filename])

class Pokemon(models.Model):
  name = models.CharField(max_length=100, blank=False, null=False)
  description = models.CharField(max_length=200, blank=True, null=False)
  type = models.ManyToManyField(Type, through="Pokemon_Type")
  skill = models.CharField(max_length=100, blank=False, null=False)
  image = models.ImageField(upload_to=nameFile, default='not-image.png', null=False)
  state = models.SmallIntegerField(default=1, null=False)
  created_at = models.DateTimeField(auto_now_add=True)
  updated_at = models.DateTimeField(auto_now=True)

  def __str__(self):
    return '{}, - {}'.format(self.name, self.skill)

  class Meta:
    db_table = 'Pokemon'
    

class Pokemon_Type(models.Model):
  pokemon = models.ForeignKey(Pokemon, on_delete=models.CASCADE)
  type = models.ForeignKey(Type, on_delete=models.CASCADE)
  state = models.SmallIntegerField(default=1, null=False)
  created_at = models.DateTimeField(auto_now_add=True)
  updated_at = models.DateTimeField(auto_now=True)
  
  def __str__(self):
    return '{} - {}'.format(self.pokemon, self.type)
  
  class Meta:
    db_table = "Pokemon_Type"
