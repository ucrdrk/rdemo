from rest_framework import serializers

from .models import Foo

class FooSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Foo
        fields = ('name',)