from django.db import models

# Create your models here.
class Info(models.Model):
    city = models.CharField(max_length=100)
    street = models.CharField(max_length=100,null=True)
    phone_number = models.CharField(max_length=20)
    work_hours = models.CharField(max_length=50,default="Mon to Fri 9am to 6pm")
    email = models.EmailField(max_length=60)
    email_pio = models.CharField(max_length=60,default="Send us your query anytime!")

    class Meta:
        verbose_name = ("Info")
        verbose_name_plural = ("Infos")

    def __str__(self):
        return self.email