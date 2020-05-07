# Serializer to convert HTTP request data sent to Django to a valid response data
# concerned with how data is returned to user
from rest_framework import serializers
from leads.models import Lead # The database part form earlier 

# Lead Serializer
class LeadSerializer(serializers.ModelSerializer):
    class Meta:
        model = Lead
        # fields = (name, email...)
        fields = '__all__' # all fields 