from django.db import models

# Create your models here.
class PresentCup(models.Model):
    id = models.CharField(max_length=100, primary_key=True)
    long = models.FloatField()
    lat = models.FloatField()
    address = models.CharField(max_length=255)
    like = models.IntegerField(default=0)
    dislike = models.IntegerField(default=0)

    # def __str__(self):
    #     msg= f'{self.id} : 좌표 {self.long} {self.lat}, 주소 {self.address}, 더러움 정도 : {self.dirty}'
    #     return msg

    class Meta:
        ordering = ['id']

# Create your models here.
class PredictCup(models.Model):
    id = models.CharField(max_length=100, primary_key=True)
    long1 = models.FloatField()
    lat1 = models.FloatField()
    long2 = models.FloatField()
    lat2 = models.FloatField()
    long3 = models.FloatField()
    lat3 = models.FloatField()
    long4 = models.FloatField()
    lat4 = models.FloatField()
    address = models.CharField(max_length=255)
    like = models.IntegerField(default=0)
    dislike = models.IntegerField(default=0)

    # def __str__(self):
    #     msg= f'{self.id} : 좌표 {self.long} {self.lat}, 주소 {self.address}, 더러움 정도 : {self.dirty}'
    #     return msg

    class Meta:
        ordering = ['id']
    