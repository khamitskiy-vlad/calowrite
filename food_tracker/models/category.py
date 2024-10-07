from django.db import models

class Category(models.Model):
    name = models.CharField(max_length=100, unique=True)

    class Meta:
        db_table = 'food_category'
        ordering = ['name']

    def __str__(self):
        return self.name
