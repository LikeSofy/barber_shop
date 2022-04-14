from datetime import timedelta

from django.contrib.auth.models import User
from django.core.validators import MinValueValidator, MaxValueValidator, MinLengthValidator, MaxLengthValidator
from django.db import models


# 1 services
# 2 masters
# 3 appointment
from .validators import date_greater_than_present_validator


class Service(models.Model):
    name = models.CharField(max_length=50, verbose_name="Название услуги", unique=True, validators=[
        MinLengthValidator(limit_value=5, message="Название услуги должно содержать от 5 до 50 символов"),
        MaxLengthValidator(limit_value=50, message="Название услуги должно содержать от 5 до 50 символов"),
    ])
    photo = models.ImageField(upload_to='service', verbose_name="Фото")
    nums_minutes_to_complete = models.IntegerField(verbose_name="Продолжительность в минутах", validators=[
        MinValueValidator(limit_value=5, message="Продолжительность не может быть меньше 5 минут"),
        MaxValueValidator(limit_value=180, message="Продолжительность не может быть более 180 минут")
    ])
    price = models.DecimalField(max_digits=6, decimal_places=2, validators=[
        MinValueValidator(limit_value=5, message="Стоимость услуги должна быть от 5 до 1000 BYN"),
        MaxValueValidator(limit_value=1000, message="Стоимость услуги должна быть от 5 до 1000 BYN")
    ])
    slug = models.SlugField(unique=True)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = "услуга"
        verbose_name_plural = "услуги"


class Master(models.Model):
    name = models.CharField(max_length=20, verbose_name="Имя мастера", validators=[
        MinLengthValidator(limit_value=3, message="Имя должно содержать от 3 до 20 символов"),
        MaxLengthValidator(limit_value=20, message="Имя должно содержать от 3 до 20 символов"),
    ])
    photo = models.ImageField(upload_to='masters', verbose_name="Фото мастера")
    description = models.TextField(max_length=1000, verbose_name="Информация про мастера", validators=[
        MaxLengthValidator(limit_value=1000, message="Информация должна содержать не более 1000 символов"),
    ])

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = "мастер"
        verbose_name_plural = "мастера"


class Appointment(models.Model):
    master = models.OneToOneField(Master, on_delete=models.PROTECT, verbose_name="Мастер")
    service = models.OneToOneField(Service, on_delete=models.PROTECT, verbose_name="Услуга")
    start_time = models.DateTimeField(verbose_name="Дата и время записи", validators=[
        date_greater_than_present_validator
    ])
    end_time = models.DateTimeField()
    user = models.ForeignKey(User, on_delete=models.CASCADE)

    def clean(self):
        start_time = self.time
        end_time = start_time + timedelta(minutes=self.service.nums_minutes_to_complete)
        ending_appointment = Appointment.objects.filter(end_time__range=(start_time, end_time))
        starting_appointment = Appointment.objects.filter(start_time__range=(start_time, end_time))
        models.Model.clean(self)

    def __str__(self):
        return "{} - {}".format(self.master.name, self.service.name)

    class Meta:
        verbose_name = "запись"
        verbose_name_plural = "записи"
