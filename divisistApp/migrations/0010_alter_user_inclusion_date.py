# Generated by Django 5.1.2 on 2024-11-27 23:55

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('divisistApp', '0009_user_inclusion_date'),
    ]

    operations = [
        migrations.AlterField(
            model_name='user',
            name='inclusion_date',
            field=models.DateField(default='2024-01-01'),
        ),
    ]