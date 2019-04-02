from django.db import models

class Customer(models.Model):
    name=models.CharField(max_length=250)
    age=models.IntegerField()
    mobile=models.CharField(max_length=30)
    email=models.CharField(max_length=200)
    address=models.CharField(max_length=200)
    username=models.CharField(max_length=200)
    password=models.CharField(max_length=200)

    def __str__(self):
        return self.name


class AdminInfo(models.Model):
    name = models.CharField(max_length=250)
    age = models.IntegerField()
    mobile = models.CharField(max_length=30)
    email = models.CharField(max_length=200)
    address = models.CharField(max_length=200)
    username = models.CharField(max_length=200)
    password = models.CharField(max_length=200)

    def __str__(self):
        return self.name

class RegisterPackageInfo(models.Model):
    name=models.CharField(max_length=250)
    gender=models.CharField(max_length=250)
    age=models.IntegerField()
    mobile=models.IntegerField()
    package_name=models.CharField(max_length=200)
    email=models.CharField(max_length=250)
    user_name=models.CharField(max_length=200)



    def __str__(self):
        return self.name

class PackageCosts(models.Model):
    packagename=models.CharField(max_length=200,null=True)
    cost=models.IntegerField()

    def __str__(self):
        return self.packagename

class MyBankDetails(models.Model):
    name=models.CharField(max_length=200)
    email=models.CharField(max_length=200)
    card_number=models.IntegerField()
    balance=models.IntegerField()

    def __str__(self):
        return self.name

class Shedule(models.Model):
    package_name=models.CharField(max_length=200)
    date=models.DateField()
    time=models.TimeField()

    def __str__(self):
        return self. package_name



class PaymentStatus(models.Model):
    status=models.CharField(max_length=200)

    def __str__(self):
        return self.status



