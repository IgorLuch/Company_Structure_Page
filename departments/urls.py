from django.urls import path
from .views import index, department_detail, employee_detail, add_employee

urlpatterns = [
    path('', index, name='index'),
    path('department/<int:department_id>/', department_detail, name='department-detail'),
    path('employee/<int:employee_id>/', employee_detail, name='employee-detail'),
    path('add-employee/', add_employee, name='add-employee'),  # Новый маршрут
]
