from django.db import models
# we dont have the model for user that we created but django does so we just include it
from django.contrib.auth.models import User

# Create your models here.

class Product(models.Model):
	title = models.CharField(max_length=255)
	pub_date = models.DateTimeField()
	body = models.TextField()
	url = models.TextField()
	image = models.ImageField(upload_to='images/')
	icon = models.ImageField(upload_to='images/')
	votes_total = models.IntegerField(default=1)
	# hunter is a person who has submitted or found the product
	hunter = models.ForeignKey(User, on_delete = models.CASCADE)
	# so here we are assigning an id to hunter and this id will be a foreignkey referencing the user table 
	# and we have used ON DELETE CASCADE in case of any deletes

	def __str__(self):
		return self.title

	def summary(self):
	 	return self.body[:100] # slicing body and taking 1st 100 chars only

	def pub_date_pretty(self):
		return self.pub_date.strftime('%b %e %Y')


# no do :
# python manage.py makemigrations
# python manage.py migrate