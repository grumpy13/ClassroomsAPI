from rest_framework import serializers
from classes.models import Classroom

class ClassroomListSerializer(serializers.ModelSerializer):
    class Meta:
        model = Classroom
        fields = [
            'id',
            'subject',
            'year',
            'teacher',

            ]


class ClassroomDetailSerializer(serializers.ModelSerializer):
    class Meta:
        model = Classroom
        fields = [
            'name',
            'subject',
            'teacher',
            'year',
            ]

class ClassroomCreateUpdateSerializer(serializers.ModelSerializer):
    class Meta:
        model = Classroom
        fields = [
            'name',
            'subject',
            'year',
            ]