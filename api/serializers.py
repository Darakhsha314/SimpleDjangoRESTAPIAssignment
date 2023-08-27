from rest_framework import serializers
from .models import Tasklist


# Create a TaskListSerializer class

class TaskListsSerializer(serializers.ModelSerializer):
    class Meta:
        model = Tasklist
        fields = ['__all__ ']
