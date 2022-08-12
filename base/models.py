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
        ("housing", "Housing"),
        ("transportation", "Transportation"),
        ("food", "Food"),
        ("utilities", "Utilities"),
        ("insurance", "Insurance"),
        ("medical", "Medical & Healthcare"),
        ("debt", "Dept Payments"),
        ("personal", "Personal Spending")]
    category = models.CharField(max_length=15, choices=category_choices, default="housing")
    sub_category = models.CharField(max_length=200, null=True, blank=True)
    amount = models.FloatField(validators=[validate_positive])
    date = models.DateField(auto_now_add=True)

    def __str__(self):
        return self.category + ": " + str(self.amount) + " $"

    class Meta:
        ordering = ["date"]



