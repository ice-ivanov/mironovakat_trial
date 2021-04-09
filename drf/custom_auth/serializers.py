from rest_framework import serializers

from .models import User


class UserSerializer(serializers.ModelSerializer):

    class Meta:
        model = User
        fields = ['id', 'username']

    def create(self, validated_data):
        user = User(
            username=validated_data['username'],
        )
        user.save()
        return user

    def update(self, request, *args):
        user = User.objects.filter(pk=request.id).first()
        user.username = args[0]['username']
        user.save()
        return user
