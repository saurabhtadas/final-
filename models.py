from django.db import models
from django.db.models import Sum

# Create your models here.
class Menu(models.Model):
	MENU_TYPE = [
		('Veg', 'Veg'),
		('Non-Veg', 'Non-Veg'),
	]
	menuType = models.CharField(max_length=191, choices = MENU_TYPE, default = None)
	menu_image = models.ImageField(upload_to='menuType')
	menu = models.CharField(max_length=191, null=True)

	def __str__(self):
		return self.menu

class Cuisines(models.Model):
	MENU_TYPE = [
		('Veg', 'Veg'),
		('Non-Veg', 'Non-Veg'),
	]
	menuType = models.CharField(max_length=191, choices = MENU_TYPE, default = None)
	dish_type = models.ForeignKey(Menu, on_delete = models.CASCADE)
	dish_image = models.ImageField(upload_to='dish')
	dish_name = models.CharField(max_length=191)
	cost = models.IntegerField(default=0)

	def __str__(self):
		return self.dish_name

class Cart(models.Model):
	MENU_TYPE = [
		('Veg', 'Veg'),
		('Non-Veg', 'Non-Veg'),
	]
	menuType = models.CharField(max_length=191, choices = MENU_TYPE, default = None)
	dish_type = models.ForeignKey(Menu, on_delete = models.CASCADE)
	dish_name = models.CharField(max_length=191)
	unit_price = models.IntegerField(default=0)
	cost = models.IntegerField(default=0)
	quantity = models.IntegerField(default=1)
	username = models.CharField(max_length=191)
	contact_no = models.CharField(max_length=191, default=0)
	table_no = models.IntegerField(default=0)

	def __str__(self):
		return self.dish_name + '-' + self.username + '-' + str(self.cost)


class Staff(models.Model):
	name = models.CharField(max_length=191)
	email = models.CharField(max_length=191)
	contact_no = models.CharField(max_length=191)
	age = models.CharField(max_length=191)
	address = models.TextField()

	def __str__(self):
		return self.name
