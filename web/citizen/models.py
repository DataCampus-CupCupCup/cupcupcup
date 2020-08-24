from django.db import models

# Create your models here.
class PresentCup(models.Model):
    id = models.CharField(max_length=100, primary_key=True)
    long = models.FloatField()
    lat = models.FloatField()
    address = models.CharField(max_length=255)
    dirty = models.IntegerField(default=0)
    
    # def __str__(self):
    #     msg= f'{self.id} : 좌표 {self.long} {self.lat}, 주소 {self.address}, 더러움 정도 : {self.dirty}'
    #     return msg

    class Meta:
        ordering = ['id']
    