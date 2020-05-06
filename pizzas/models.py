from django.db import models
from django.contrib.auth.models import User

# Create your models here.

class Pizza(models.Model):
    name = models.CharField(max_length=200)
    owner = models.ForeignKey(User, on_delete=models.CASCADE)

    def __str__(self):
        return self.name

class Topping(models.Model):
    Pizza = models.ForeignKey(Pizza, on_delete=models.CASCADE)
    name = models.TextField()

    class Mate:
        verbose_name_plural = 'toppings'
    
    def __str__(self):
        return f"{self.name[:50]}..."


class Comment(models.Model):
    pizza = models.ForeignKey(Pizza, on_delete=models.CASCADE)
    text = models.TextField()
    class Mate:
        verbose_name_plural = 'Comments'
    
    def __str__(self):
        return f"{self.text[:50]}..."