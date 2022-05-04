from rest_framework import serializers
from .models import Alert, Stacks

class AlertSerial(serializers.ModelSerializer):
	class Meta:
		model = Alert
		fields = '__all__'


class StacksSerial(serializers.ModelSerializer):
	class Meta:
		model = Stacks
		fields = '__all__'