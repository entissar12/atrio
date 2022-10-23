from datetime import datetime
from django.db import models
from django.core.exceptions import ValidationError
from dateutil.relativedelta import relativedelta


def validate_date_naissance(value):
	today = datetime.now().date()
	if relativedelta(today, value).years > 150:
		raise ValidationError("personne saisie a plus que 150 ans")


# Create your models here.
class  Personne(models.Model):
	nom = models.CharField(max_length=30)
	prenom = models.CharField(max_length=30)
	date_naissance = models.DateField(validators=[validate_date_naissance])

