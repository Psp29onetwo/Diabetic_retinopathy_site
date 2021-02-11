from django.db import models
# Create your models here.


class Patient(models.Model):
    name = models.CharField(max_length=200, null=True)
    email = models.CharField(max_length=200, null=True)
    address = models.CharField(max_length=128)
    dob = models.DateField(auto_now=False, auto_now_add=False)
    phone_number = models.CharField(max_length=200, null=True)

    def __str__(self):
        return self.name


class Doctor(models.Model):
    name = models.CharField(max_length=200, null=True)
    email = models.EmailField(max_length=254)
    address = models.CharField(max_length=128)
    phone_number = models.CharField(max_length=200, null=True)

    def __str__(self):
        return self.name


class Opthalmologist(models.Model):
    name = models.CharField(max_length=200, null=True)
    email = models.EmailField(max_length=254)
    address = models.CharField(max_length=128)
    phone_number = models.CharField(max_length=200, null=True)

    def __str__(self):
        return self.name


class Patienthistory(models.Model):
    STATUS = (
        ('Recovered', 'Recovered'),
        ('Not Recovered', 'Not Recovered')
    )
    name = models.CharField(max_length=200, null=True)
    disease = models.CharField(max_length=200, null=True)
    disease_doctor = models.CharField(max_length=200, null=True)
    recovery_status = models.CharField(
        max_length=200, null=True, choices=STATUS)
    prescriptions = models.CharField(max_length=200)

    def __str__(self):
        return self.name
