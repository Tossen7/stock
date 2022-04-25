import email
from email.policy import default
from multiprocessing.sharedctypes import Value
from tkinter import CASCADE
from django.db import models

# Create your models here.

CHOICES = (
	("1", "Available"),
	("2", "Not Available")
)

WEIGHT = (
	("1", "Box"),
	("2", "Pieces")
)

class Brand(models.Model):
	name = models.CharField(max_length=255)

	def __str__(self):
		return self.name

class Category(models.Model):
	name = models.CharField(max_length=255)
	status = models.CharField(max_length=10, choices=CHOICES)

	def __str__(self):
		return self.name

	
class Product(models.Model):
	date = models.DateField(auto_now_add=True)
	category = models.ForeignKey(Category, on_delete=models.CASCADE)
	name = models.CharField(max_length=255)
	description = models.CharField(max_length = 255, default = "None")
	# image = models.ImageField(upload_to="media/product/images/")
	quantity = models.IntegerField(default=0)
	weight = models.CharField(max_length=10, choices = WEIGHT, default=1)

	def __str__(self):
		return self.name



class Member(models.Model):
	firstname = models.CharField(max_length=250, default="Tharcisse")
	lastname = models.CharField(max_length=250, default="MUNYANEZA")
	username = models.CharField(max_length=250, default="Tossen")
	profile_pic = models.ImageField(default = 'dark-souls.jpg', upload_to = 'media')
	email = models.EmailField()
	password = models.CharField(max_length=250, null=False)
	comfirm_password = models.CharField(max_length=250, null=False)
	address = models.CharField(max_length=500)

	def __str__(self) -> str:
		return self.firstname


class Order(models.Model):
	user = models.ForeignKey(Member, on_delete=models.CASCADE, default = 1)
	product = models.ForeignKey(Product, on_delete=models.CASCADE, default=1)
	number = models.IntegerField()
	date = models.DateField(auto_now_add=True)

	def __str__(self) -> str:
		return self.user


class OrderItem(models.Model):
	order_id = models.ForeignKey(Order, on_delete=models.CASCADE)
	product_id = models.ForeignKey(Product, on_delete=models.CASCADE)

	quantity = models.IntegerField()
	rate = models.FloatField(max_length=100)
	total = models.FloatField(max_length=100)
	status = models.IntegerField()


