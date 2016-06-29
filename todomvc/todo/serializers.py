from rest_framework import serializers
from todo.models import ToDos





class ToDosSerializer(serializers.ModelSerializer):

    class Meta:
        model = ToDos
        fields = ['id','title','completed','order']
