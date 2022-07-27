from rest_framework import serializers
from django.contrib.auth.models import User,Group as BaseGroup
from .models import *

class MentorSerializer(serializers.ModelSerializer):
    class Meta:
        model = Mentor
        fields = '__all__'    
    
class GroupSerializer(serializers.ModelSerializer):
    class Meta:
        model = Group
        fields = '__all__'
        
class StudentSerilizer(serializers.ModelSerializer):
    class Meta:
        model = Student
        fields = '__all__'
        
class UserSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = User
        fields = ['url', 'username', 'email', 'is_staff']
        
class BaseGroupSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = BaseGroup
        fields = ['url', 'name']
        
