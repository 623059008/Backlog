from django.contrib.auth.models import User, Group
from thing.models import Thing
from rest_framework import serializers

class UserSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = User
        fields = ('url', 'username', 'email', 'groups')

class GroupSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Group
        fields = ('url', 'name')
class ThingSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Thing
        fields = ('id', 'name', 'detail', 'time', 'status', 'priority', 'type')
    def create(self, validated_data):
        thing = Thing(
            name=validated_data['name'],
            detail=validated_data['detail'],
            time=validated_data['time'],
            status=validated_data['status'],
            priority=validated_data['priority'],
            type=validated_data['type'],
        )
        thing.save()
        return thing
    def update(self, instance, validated_data):
        """
        Update and return an existing `Snippet` instance, given the validated data.
        """
        instance.name = validated_data.get('name', instance.name)
        instance.detail = validated_data.get('detail', instance.detail)
        instance.time = validated_data.get('time', instance.time)
        instance.status = validated_data.get('status', instance.status)
        instance.priority = validated_data.get('priority', instance.priority)
        instance.type = validated_data.get('type', instance.type)
        instance.save()
        return instance
