# Generated by Django 5.1.2 on 2024-11-27 23:42

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('divisistApp', '0007_subject_prerequisites'),
    ]

    operations = [
        migrations.AddField(
            model_name='user',
            name='address',
            field=models.CharField(max_length=200, null=True),
        ),
        migrations.AddField(
            model_name='user',
            name='cellphone',
            field=models.CharField(max_length=50, null=True),
        ),
        migrations.AddField(
            model_name='user',
            name='telephone',
            field=models.CharField(max_length=50, null=True),
        ),
    ]
