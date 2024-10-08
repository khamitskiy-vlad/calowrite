from django.db import models
from .diary import Diary
from .meal_type import MealType
from django.core.validators import MinValueValidator

class Meal(models.Model):
    diary = models.ForeignKey(
        Diary,
        related_name='meals',
        on_delete=models.CASCADE
    )
    meal_type = models.ForeignKey(MealType, on_delete=models.CASCADE)
    calories = models.FloatField(validators=[MinValueValidator(0)])
    created_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ['created_at']

    def __str__(self):
        return f'{self.meal_type.name()} - {self.calories} kcal'
