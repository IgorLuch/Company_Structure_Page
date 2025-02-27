from django.shortcuts import render, get_object_or_404, redirect
from .models import Department, Employee
from .forms import EmployeeForm


def index(request):
    root_departments = Department.objects.filter(parent__isnull=True)
    return render(request, 'departments/index.html', {'root_departments': root_departments})

def department_detail(request, department_id):
    department = get_object_or_404(Department, id=department_id)
    sub_departments = Department.objects.filter(parent=department)
    employees = department.employee_set.all()
    return render(request, 'departments/department_tree.html', {
        'department': department,
        'sub_departments': sub_departments,
        'employees': employees,
    })

def employee_detail(request, employee_id):
    employee = get_object_or_404(Employee, id=employee_id)
    return render(request, 'departments/employee_detail.html', {'employee': employee})

def add_employee(request):
    if request.method == 'POST':
        form = EmployeeForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('index')
    else:
        form = EmployeeForm()
    return render(request, 'departments/add_employee.html', {'form': form})
