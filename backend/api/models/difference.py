from django.db import models

class Difference(models.Model):
    value = models.CharField(max_length=200)
    number = models.IntegerField()
    occurences = models.IntegerField()
    created_at = models.DateTimeField(auto_now_add=True)


    def __str__(self):
	       return self.value
