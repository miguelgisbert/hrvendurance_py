from django.db import models

class user(models.Model):
    name = models.CharField(max_length=100)
    birth_date = models.DateField()
    email = models.EmailField()

class record(models.Model):
    hrv_value = models.IntegerField()
    date = models.DateField()
    type = models.CharField(
        max_length= 50,
        choices=[
            ("DR", "Daily Record"),
            ("MR", "Morning Record"),
            ("BT", "Before Training"),
            ("AT", "After Training"),
            ("AT5", "5 min After Training"),
            ("AT15", "15 min After Training"),
            ("AT30", "30 min After Training")], 
            default= "DR")
