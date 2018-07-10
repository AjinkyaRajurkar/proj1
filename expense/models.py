from django.db import models
class datatable2(models.Model):
    roomid=models.IntegerField(primary_key=True)
    food = models.IntegerField()
    trip = models.IntegerField()
    shopping = models.IntegerField()


