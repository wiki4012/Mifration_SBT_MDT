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
class ZsbtMasterMembersSerializer(serializers.ModelSerializer):
	class Meta:
		model = ZsbtMasterMembers
		fields ='__all__'
class ZkpiManualDateSerializer(serializers.ModelSerializer):
	class Meta:
		model = ZkpiManualDate
		fields ='__all__'
class ZsbtAttendanceSerializer(serializers.ModelSerializer):
	class Meta:
		model = ZsbtAttendance
		fields ='__all__'
class ZsbtBannerDetailsSerializer(serializers.ModelSerializer):
	class Meta:
		model = ZsbtBannerDetails
		fields ='__all__'
class ZsbtCaPaSerializer(serializers.ModelSerializer):
	class Meta:
		model = ZsbtCaPa
		fields ='__all__'
class ZsbtCapa5WhySerializer(serializers.ModelSerializer):
	class Meta:
		model = ZsbtCapa5Why
		fields ='__all__'
class ZsbtCapaActionableSerializer(serializers.ModelSerializer):
	class Meta:
		model = ZsbtCapaActionable
		fields ='__all__'
class ZsbtCapaRecordsMasterSerializer(serializers.ModelSerializer):
	class Meta:
		model = ZsbtCapaRecordsMaster
		fields ='__all__'
class ZsbtMasterKpiSerializer(serializers.ModelSerializer):
	class Meta:
		model = ZsbtMasterKpi
		fields ='__all__'
class ZsbtMdtEscalationsSerializer(serializers.ModelSerializer):
	class Meta:
		model = ZsbtMdtEscalations
		fields ='__all__'
class ZsbtMeetingAgendaTableSerializer(serializers.ModelSerializer):
	class Meta:
		model = ZsbtMeetingAgendaTable
		fields ='__all__'
class ZsbtShiftActiveSerializer(serializers.ModelSerializer):
	class Meta:
		model = ZsbtShiftActive
		fields ='__all__'
class ZsbtShiftBasedSerializer(serializers.ModelSerializer):
	class Meta:
		model = ZsbtShiftBased
		fields ='__all__'
class ZsbtStarSerializer(serializers.ModelSerializer):
	class Meta:
		model = ZsbtStar
		fields ='__all__'