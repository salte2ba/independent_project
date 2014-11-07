from django.db import models

class Add_person(models.Model):
	DROP_CHOICES = (
	('1','No Skill'),
	('2','Below Average'),
	('3','Average'),
	('4','Above Average'), 
	('5','Pro'),
	)
	SHIRT_CHOICES = (
	('S', 'S'),
	('M', 'M'),
	('L', 'L'),
	)
	POSITION_CHOICES = (
	('1', 'In Cutter'),
	('2', 'Out Cutter'),
	('3', 'Short Distance Handler'),
	('4', 'Long Distance Handler'),
	)
	first_name = models.CharField(max_length =200)
	last_name = models.CharField(max_length=200)
	sex = models.CharField(max_length=1, choices=(('M','Male'),('F','Female')))
	email = models.CharField(max_length=200)
	phone = models.CharField(max_length=10)
	skills = models.CharField(max_length=1, choices = DROP_CHOICES)
	wants_shirt = models.BooleanField(default=False)
	wants_frisbee = models.BooleanField(default=False)
	shirtsize = models.CharField(max_length=1, choices = SHIRT_CHOICES, default='L')
	position = models.CharField(max_length=1, choices= POSITION_CHOICES, default='1')
	def __str__(self):
		return self.first_name + " " + self.last_name

