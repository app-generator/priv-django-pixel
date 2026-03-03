from django.db import models
from django.contrib.auth.models import User


class Client(models.Model):
    """Model przechowujący dane klientów freelancera."""
    name = models.CharField(max_length=255)
    company = models.CharField(max_length=255, blank=True)
    email = models.EmailField()

    def __str__(self):
        return self.name


class Project(models.Model):
    """Model przechowujący szczegóły projektów."""
    STATUS_CHOICES = [
        ('idea', 'Pomysł'),
        ('coding', 'W trakcie'),
        ('testing', 'Testowanie'),
        ('done', 'Zakończone'),
    ]
    
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    client = models.ForeignKey(
        Client, 
        on_delete=models.CASCADE, 
        related_name='projects'
    )
    title = models.CharField(max_length=255)
    description = models.TextField(blank=True)
    deadline = models.DateField()
    status = models.CharField(
        max_length=20, 
        choices=STATUS_CHOICES, 
        default='idea'
    )

    def __str__(self):
        return self.title