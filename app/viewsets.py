from .serializers import *
from rest_framework import viewsets
from django.db.models.functions import Lower


# ViewSets define the view behavior.
class PersonneViewSet(viewsets.ModelViewSet):
    queryset = Personne.objects.all().order_by(Lower("nom"))
    serializer_class = PersonneSerializer
