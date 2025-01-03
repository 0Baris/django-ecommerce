# Generated by Django 5.1.4 on 2024-12-25 12:24

import django.core.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('user', '0003_order'),
    ]

    operations = [
        migrations.AddField(
            model_name='address',
            name='phone_number',
            field=models.CharField(default='+900000000000', max_length=15, validators=[django.core.validators.RegexValidator(message="Telefon numarası için kullanılması gereken format: '+999999999'.", regex='^\\+?1?\\d{9,15}$')]),
        ),
    ]
