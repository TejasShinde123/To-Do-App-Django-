from django.db import models
from django.contrib.auth.models import User

class TODOO(models.Model):
    STATUS_CHOICES = (
        ('OPEN', 'Open'),
        ('WORKING', 'Working'),
        ('PENDING_REVIEW', 'Pending Review'),  # Improved readability
        ('COMPLETED', 'Completed'),
        ('OVERDUE', 'Overdue'),
        ('CANCELLED', 'Cancelled'),
    )

    srno = models.AutoField(primary_key=True, auto_created=True)
    title = models.CharField(max_length=100)
    description = models.CharField(max_length=1000)
    date = models.DateTimeField(auto_now_add=True)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    due_date = models.DateField(null=True, blank=True)  # Corrected typo
    status = models.CharField(max_length=20, choices=STATUS_CHOICES, default='OPEN')
    tag = models.CharField(max_length=25)

    def get_status_display(self):
        return self.status.capitalize()  # Improved capitalization