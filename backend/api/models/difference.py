from django.db import models
from django.core.validators import MaxValueValidator, MinValueValidator

class Difference(models.Model):
    value = models.IntegerField()
    number = models.IntegerField(validators=[
            MaxValueValidator(100),
            MinValueValidator(1)
        ])
    occurences = models.IntegerField()
    created_at = models.DateTimeField(auto_now_add=True)


    def __str__(self):
	       return self.value
