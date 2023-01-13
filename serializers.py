from rest_framework import serializers
from .models import student
class student_serialzer(serializers.Serializer):
    first_name = serializers.CharField(max_length = 30)
    last_name = serializers.CharField(max_length = 30)
    roll_no = serializers.IntegerField()
    city = serializers.CharField(max_length = 30)

    def create(self, validated_data):
        return student.objects.create(**validated_data)
    
    def update(self,instance,validated_data):
        instance.first_name = validated_data.get('first_name', instance.first_name)
        instance.last_name = validated_data.get('last_name', instance.last_name)
        instance.save()
        return instance 

    def validate_roll_no(self,value):
        if value >= 200:
            raise serializers.ValidationError('Seat full')
        return value