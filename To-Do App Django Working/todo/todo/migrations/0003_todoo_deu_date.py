# Generated by Django 4.2.4 on 2024-12-04 07:52

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('todo', '0002_todoo_description_alter_todoo_title'),
    ]

    operations = [
        migrations.AddField(
            model_name='todoo',
            name='deu_date',
            field=models.DateField(blank=True, null=True),
        ),
    ]