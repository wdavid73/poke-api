from django.db import models
from poke_api.Type.Model.ModelType import Type

def nameFile(instace, filename):
  return '/'.join(['images','pokemon', filename])

class Pokemon(models.Model):
  name = models.CharField(max_length=100, blank=False, null=False)
  description = models.CharField(max_length=200, blank=True, null=False)
  type= models.ForeignKey(
    Type, db_column="type_id", on_delete=models.CASCADE, null=False
  )
  skill = models.CharField(max_length=100, blank=False, null=False)
  image = models.ImageField(upload_to=nameFile, default='not-image.png', null=False)
  state = models.SmallIntegerField(default=1, null=False)
  created_at = models.DateTimeField(auto_now_add=True)
  updated_at = models.DateTimeField(auto_now=True)

  def __str__(self):
    return '{}, {} - {}'.format(self.name, self.type, self.skill)

  class Meta:
    db_table = 'Pokemon'
