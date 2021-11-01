from rest_framework.serializers import ModelSerializer
from rest_framework import serializers
from .models import User, Lead, Message


class MessageSerializer(ModelSerializer):
    class Meta:
        model = Message
        fields = '__all__'


class LeadSerializer(ModelSerializer):
    class Meta:
        model = Lead
        fields = '__all__'


class EnumField(serializers.ChoiceField):
    def __init__(self, enum, **kwargs):
        self.enum = enum
        kwargs['choices'] = [(e.name, e.name) for e in enum]
        super(EnumField, self).__init__(**kwargs)

    def to_representation(self, obj):
        return obj.name

    def to_internal_value(self, data):
        try:
            return self.enum[data]
        except KeyError:
            self.fail('invalid_choice', input=data)


class UserSerializer(ModelSerializer):
    class Meta:
        model = User
        fields = ['email', 'firstName', 'lastName', 'phoneNumber', 'password', 'is_active']
        extra_kwargs = {
            'password': {'write_only': True}
        }

    def create(self, validated_data):
        password = validated_data.pop('password', None)
        instance = self.Meta.model(**validated_data)
        if password is not None:
            instance.set_password(password)
        instance.save()
        return instance


class AdminSerializer(ModelSerializer):
    class Meta:
        model = User
        fields = ['email', 'firstName', 'lastName', 'phoneNumber', 'password', 'is_superuser']
        extra_kwargs = {
            'password': {'write_only': True}
        }

    def create(self, validated_data):
        password = validated_data.pop('password', None)
        instance = self.Meta.model(**validated_data)
        if password is not None:
            instance.set_password(password)
        instance.save()
        return instance