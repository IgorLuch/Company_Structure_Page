from django.db import models

class Department(models.Model):
    name = models.CharField(max_length=100, verbose_name="Название отдела")
    parent = models.ForeignKey('self', on_delete=models.CASCADE, null=True, blank=True, verbose_name="Родительский отдел")

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = "Отдел"
        verbose_name_plural = "Отделы"

class Employee(models.Model):
    last_name = models.CharField(max_length=100, verbose_name="Фамилия")
    first_name = models.CharField(max_length=100, verbose_name="Имя")
    middle_name = models.CharField(max_length=100, verbose_name="Отчество", blank=True, null=True)
    position = models.CharField(max_length=100, verbose_name="Должность")
    hire_date = models.DateField(verbose_name="Дата приема на работу")
    salary = models.DecimalField(max_digits=10, decimal_places=2, verbose_name="Зарплата")
    department = models.ForeignKey(Department, on_delete=models.CASCADE, verbose_name="Отдел")

    def __str__(self):
        return f"{self.last_name} {self.first_name} {self.middle_name or ''}"

    class Meta:
        verbose_name = "Сотрудник"
        verbose_name_plural = "Сотрудники"
        