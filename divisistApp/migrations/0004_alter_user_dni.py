# Generated by Django 5.1.2 on 2024-10-31 00:06

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('divisistApp', '0003_remove_user_institutional_email_password'),
    ]

    operations = [
        migrations.AlterField(
            model_name='user',
            name='dni',
            field=models.CharField(default='0', max_length=12, unique=True),
        ),
    ]
