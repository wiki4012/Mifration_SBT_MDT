from rest_framework import serializers
from .models import *

class ZsbtMasterTeamsSerializer(serializers.ModelSerializer):
	class Meta:
		model = ZsbtMasterTeams
		fields ='__all__'

class ZsbtTriggerHitCasesSerializer(serializers.ModelSerializer):
	class Meta:
		model = ZsbtTriggerHitCases
		fields ='__all__'

