from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User

DOSAGE_UNIT_CHOICES = [
    ('Drop', 'Drop'),
    ('Pill', 'Pill'),
    ('Tablet', 'Tablet'),
    ('Vial', 'Vial'),
    ('Others', 'Others'),
]

FREQ_CHOICES = [
    ('Daily', 'Daily'),
    ('Weekly', 'Weekly'),
    ('Monthly', 'Monthly'),
]

FREQ_UNIT_CHOICES = [
    ('Once', 'Once'),
    ('Twice', 'Twice'),
    ('Trice', 'Trice'),
    ('Others', 'Others'),
]


class Medicine(models.Model):
    user = models.ManyToManyField(User)
    medicine_name = models.CharField(max_length=100)
    dosage = models.IntegerField()
    dosage_unit = models.CharField(max_length=100,
                                   choices=DOSAGE_UNIT_CHOICES,
                                   default="DROP")
    frequency = models.CharField(max_length=100,
                                 choices=FREQ_CHOICES,
                                 default="DAILY")
    frequency_unit = models.CharField(max_length=100,
                                      choices=FREQ_UNIT_CHOICES,
                                      default="ONCE")
    created_at = models.DateTimeField(default=timezone.now)

    def __str__(self):
        return self.medicine_name
