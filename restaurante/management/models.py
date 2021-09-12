from django.db import models
from django.db.models.deletion import PROTECT

from management.constants import *
from management.utils import validate_cpf

class Department(models.Model):
    name = models.CharField("nome", max_length=50)
    acronym = models.CharField("sigla", max_length=30, unique=True)

    def __str__(self) -> str:
        return self.name

class Course(models.Model):
    name = models.CharField("nome", max_length=50)
    acronym = models.CharField("sigla", max_length=50, unique=True)
    department = models.ForeignKey(Department, on_delete=models.PROTECT)

    def __str__(self) -> str:
        return self.name

class Consumer(models.Model):
    name = models.CharField("nome completo", max_length=50)
    cpf = models.CharField("cpf", max_length=11, unique=True, validators=[validate_cpf])
    type = models.CharField("tipo", max_length=30, choices=CONSUMERS_TYPES)
    registration = models.CharField("matrícula", max_length=50)
    gender = models.CharField("genero", max_length=30, choices=GENDERS)
    year_of_entry = models.IntegerField("ano de ingresso")
    title = models.CharField("título", max_length=30, choices=TITLES)

    def __str__(self) -> str:
        return self.name

class Student(models.Model):
    course = models.ForeignKey(Course, on_delete=models.PROTECT)
    consumer = models.ForeignKey(Consumer, on_delete=models.CASCADE)

class Employee(models.Model):
    department = models.ForeignKey(Department, on_delete=models.PROTECT)
    consumer = models.ForeignKey(Consumer, on_delete=models.CASCADE)

class Meal(models.Model):
    type = models.CharField("tipo", max_length=50)
    shift = models.CharField("turno", max_length=50, choices=SHIFTS)
    description = models.TextField("descrição", max_length=200)
    vegeterian_option = models.TextField("opção vegeratiana", max_length=200)

    def save(self, *args, **kwargs):
        self.type = MEAL_TYPES[self.shift]
        super().save(*args, **kwargs)

class Ticket(models.Model):
    price = models.FloatField("preço")
    meal = models.ForeignKey(Meal, on_delete=models.PROTECT)
    consumer = models.ForeignKey(Consumer, on_delete=PROTECT)
    paid = models.BooleanField("pago", default=False)

    def save(self, *args, **kwargs):
        consumer_type = self.consumer.type
        meal_type = self.meal.shift
        self.price = PRICES[meal_type].get(consumer_type)
        super().save(*args, **kwargs)