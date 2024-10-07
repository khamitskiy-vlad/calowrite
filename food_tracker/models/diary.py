from django.db import models
from django.db.models.signals import post_save
from django.dispatch import receiver
from django.core.validators import MinValueValidator
from .meal import Meal

class Diary(models.Model):
    created_at = models.DateTimeField(auto_now_add=True)
    calories = models.FloatField(validators=[MinValueValidator(0)])

    class Meta:
        db_table = 'food_diary'
        ordering = ['created_at']

    def __str__(self):
        return f'Diary created at {self.created_at}'

@receiver(post_save, sender=Meal)
def update_diary_calories(sender, instance, **kwargs):
    diary = instance.diary
    total_calories = sum(meal.calories for meal in diary.meals.all())
    diary.calories = total_calories
    diary.save
