from django.db import models


# Create your models here.
class Loan(models.Model):
  name = models.CharField(max_length=250)
  amount = models.DecimalField(max_digits=10, decimal_places=2)
  created = models.DateTimeField(auto_now_add=True)
  date = models.DateField()
  reason = models.TextField()

  def __str__(self):
    return f"{self.name} - {self.amount}"