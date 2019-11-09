# coding:utf-8


from django.db import models


class Position(models.Model):
	asset = models.CharField(max_length = 10)
	timestamp = models.DataTimeField()
	amount = models.DecimalField(max_digits = 10, decimal_places = 3)
	