from django.db import models

# Create your models here.
class Aplication(models.Model):
    app_name = models.CharField(max_length=50)
    domain_name = models.CharField(max_length=50)
    email = models.EmailField()
    requirement = models.CharField(max_length=100)
    def __str__(self):

        return ' '.join([
            self.app_name,
            self.domain_name,
            self.email,
            self.requirement,
        ])
class Accept(models.Model):
    app_name = models.CharField(max_length=50)
    domain_name = models.CharField(max_length=50)
    email = models.EmailField()
    requirement = models.CharField(max_length=100)
    def __str__(self):

        return ' '.join([
            self.app_name,
            self.domain_name,
            self.email,
            self.requirement,
        ])
class Reject(models.Model):
    app_name = models.CharField(max_length=50)
    domain_name = models.CharField(max_length=50)
    email = models.EmailField()
    requirement = models.CharField(max_length=100)
    def __str__(self):

        return ' '.join([
            self.app_name,
            self.domain_name,
            self.email,
            self.requirement,
        ])