from rest_framework import serializers
from jsonToElasticParser.models import Model


class ModelSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Model
        fields = ['name',  'content', 'created', 'last_updated',]
