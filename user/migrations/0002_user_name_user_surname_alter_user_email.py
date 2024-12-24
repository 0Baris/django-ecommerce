# Generated by Django 5.1.4 on 2024-12-24 11:17

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('user', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='user',
            name='name',
            field=models.CharField(default='Default Name', max_length=50),
        ),
        migrations.AddField(
            model_name='user',
            name='surname',
            field=models.CharField(default='Default Surname', max_length=50),
        ),
        migrations.AlterField(
            model_name='user',
            name='email',
            field=models.EmailField(max_length=254, unique=True),
        ),
    ]