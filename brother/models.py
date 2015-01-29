from django.db import models
class Register(models.Model):		
	username=models.CharField(max_length=20)
	password=models.CharField(max_length=20)
	conformpassword=models.CharField(max_length=20)
	age=models.IntegerField()
	phone=models.IntegerField()
	gmail=models.EmailField()