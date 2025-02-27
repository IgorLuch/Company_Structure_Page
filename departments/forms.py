from django import forms
from .models import Employee

class EmployeeForm(forms.ModelForm):
    class Meta:
        model = Employee
        fields = ['last_name', 'first_name', 'middle_name', 'position', 'hire_date', 'salary', 'department']
        widgets = {
            'hire_date': forms.DateInput(attrs={'type': 'date'}),
        }
