from rest_framework import serializers
from list.models import Quote


class QuoteSerializer(serializers.ModelSerializer):

    class Meta:
        model = Quote
        fields = ('author', 'text', 'added_date')
