from django.db import models
from django.contrib.auth.models import User
from django.core.exceptions import ValidationError

def validate_positive(value):
    if value < 0.0:
        raise ValidationError(
            ("%(value)s is not a positive number"),
            params={"value": value},
        )

class Expense(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    category_choices = [
        ("Housing", "Housing"),
        ("Transportation", "Transportation"),
        ("Food", "Food"),
        ("Utilities", "Utilities"),
        ("Insurance", "Insurance"),
        ("Medical", "Medical & Healthcare"),
        ("Debt", "Dept Payments"),
        ("Personal", "Personal Spending")]
    category = models.CharField(max_length=15, choices=category_choices, default="housing")
    sub_category = models.CharField(max_length=200)
    amount = models.FloatField(validators=[validate_positive])
    date = models.DateField(auto_now_add=True)

    def __str__(self):
        return self.category + " (" + self.sub_category + ") " ": " + str(self.amount) + " $"

    class Meta:
        ordering = ["date"]



