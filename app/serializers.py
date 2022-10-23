from dateutil.relativedelta import relativedelta
from datetime import datetime
from .models import Personne
from rest_framework import  serializers

# Serializers define the API representation.
class PersonneSerializer(serializers.HyperlinkedModelSerializer):
	def compute_age(self, obj):
		today = datetime.now().date()
		return relativedelta(today, obj.date_naissance).years

	age = serializers.SerializerMethodField("compute_age", read_only=True)

	class Meta:
		model = Personne
		fields = ['nom', 'prenom', 'date_naissance', "age"]