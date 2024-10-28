from django.contrib.auth.hashers import make_password
from rest_framework import serializers 
from .models import * 
from django.contrib.auth.models import User



class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ['id', 'username', 'password']
        # extra_kwargs = {
        #     'password': {'write_only': True, 'required': True}
        # }

    def create(self, validated_data):
        # تشفير كلمة المرور
        validated_data['password'] = make_password(validated_data['password'])
        # إنشاء المستخدم
        user = User.objects.create(**validated_data)
        return user


class MealSerializer(serializers.ModelSerializer):
    class Meta:
        model = Meal
        fields = ['id', 'title', 'description', 'no_of_ratings', 'avg_rating']



class RatingSerializer(serializers.ModelSerializer):
    class Meta:
        model = Rating
        fields = ['id', 'stars', 'user', 'meal']
