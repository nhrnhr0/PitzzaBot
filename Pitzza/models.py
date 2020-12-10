from django.db import models

# Create your models here.
class PitzzaType(models.Model):
    name = models.CharField(max_length=50, verbose_name="size",)
    piecesNum = models.IntegerField(verbose_name="number of pieces",)
    price = models.FloatField(verbose_name="cost for pitzza without extras")
    
    def __str__(self):
        return self.name
    
    pass


class PitzzaExtra(models.Model):
    image = models.ImageField(verbose_name="image",)
    name = models.CharField(verbose_name="name", max_length=50)
    price = models.FloatField(verbose_name="price to put on one slice")
    
    def __str__(self):
        return self.name
    
    pass

class Pitzza(models.Model):
    pType = models.ForeignKey(to=PitzzaType, on_delete=models.CASCADE)
    pExtras = models.ManyToManyField(to=PitzzaExtra,through='PitzzaThrough',)
    def __str__(self):
        return str(self.pType)
    
    pass

class PitzzaThrough(models.Model):
    pitzza = models.ForeignKey(to=Pitzza, on_delete=models.CASCADE)
    pitzzaExtra = models.ForeignKey(to=PitzzaExtra, on_delete=models.CASCADE)
    pieceIndex = models.IntegerField(verbose_name='piece index')
