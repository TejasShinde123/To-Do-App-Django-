# Generated by Django 4.2.4 on 2024-12-04 06:20

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('todo', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='todoo',
            name='description',
            field=models.CharField(default=django.utils.timezone.now, max_length=1000),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='todoo',
            name='title',
            field=models.CharField(max_length=100),
        ),
    ]
