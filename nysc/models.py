from django.db import models

# Create your models here.
class Database(models.Model):

    # GENDER = (
    #     ('M', 'Male'),
    #     ('F', 'Female')
    # )

    name = models.CharField(max_length=150)
    state_code = models.CharField(max_length=11)
    # gender = models.CharField(max_length=1, null=True, choices=GENDER)
    ppa = models.CharField(max_length=100)
    bank_name = models.CharField(max_length=50)
    account_number = models.CharField(max_length=10)
    # email = models.EmailField(max_length=254,)

    def __str__(self):
        return self.name

class Inec(models.Model):

    name = models.CharField(max_length=150)
    state_code = models.CharField(max_length=11)
    ppa = models.CharField(max_length=100)
    bank_name = models.CharField(max_length=50)
    account_number = models.CharField(max_length=10)

    def __str__(self):
        return self.name