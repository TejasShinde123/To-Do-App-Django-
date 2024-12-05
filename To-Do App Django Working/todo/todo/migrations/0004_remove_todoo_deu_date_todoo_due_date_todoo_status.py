# Generated by Django 4.2.4 on 2024-12-04 08:14

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('todo', '0003_todoo_deu_date'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='todoo',
            name='deu_date',
        ),
        migrations.AddField(
            model_name='todoo',
            name='due_date',
            field=models.DateField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='todoo',
            name='status',
            field=models.CharField(choices=[('OPEN', 'Open'), ('WORKING', 'Working'), ('PENDING_REVIEW', 'Pending Review'), ('COMPLETED', 'Completed'), ('OVERDUE', 'Overdue'), ('CANCELLED', 'Cancelled')], default='OPEN', max_length=20),
        ),
    ]