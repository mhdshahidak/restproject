from rest_framework import routers, serializers
from . import models

class StudentSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.student
        fields = '__all__'
        read_only_fields = ('age',)

