from rest_framework import serializers
from igs.employee.models import Employee

class EmployeeSerializer(serializers.ModelSerializer):
    class Meta:
        model = Employee
        fields = [ 'name', 'email', 'department', 'id']
