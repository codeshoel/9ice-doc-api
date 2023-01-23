from rest_framework import serializers
from .models import Stakeholder



class StakeholdersSerializer(serializers.ModelSerializer):

    class Meta:
        model = Stakeholder
        fields = [
            'id',
            'first_name',
            'last_name',
            'email',
            'mobile',
            'address',
        ]





