from django.db import models

# Create your models here.
class Insurance(models.Model):
	"""docstring for Product"""
	title = models.TextField()
	land  = models.TextField()
	# def __init__(self, arg):
	# 	super(Product, self).__init__()
	# 	self.arg = arg
		