from rest_framework import serializers
from .models import Department, Employee

class EmployeeSerializer(serializers.ModelSerializer):
    class Meta:
        model = Employee
        fields = ['id', 'name']

class DepartmentSerializer(serializers.ModelSerializer):
    employees = EmployeeSerializer(many=True, read_only=True)
    children = serializers.SerializerMethodField()

    class Meta:
        model = Department
        fields = ['id', 'name', 'parent', 'employees', 'children']

    def get_children(self, obj):
        children = Department.objects.filter(parent=obj)
        return DepartmentSerializer(children, many=True).data
    
    