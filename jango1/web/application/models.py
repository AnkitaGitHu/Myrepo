from django.db import models



# Create your models here.
class Blood(models.Model):
    patient_name = models.CharField(max_length=255)
    age = models.CharField(max_length=255)
    disease = models.CharField(max_length=255)
    blood_group=models.CharField(max_length=255)
    c_date=models.CharField(max_length=255)



class Donor(models.Model):
    donor_name = models.CharField(max_length=255)
    age = models.CharField(max_length=255)
    disease = models.CharField(max_length=255)
    blood_group=models.CharField(max_length=255)
    r_date=models.CharField(max_length=255)
