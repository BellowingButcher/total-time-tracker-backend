# Generated by Django 4.1.3 on 2022-11-28 16:51

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('myapp', '0002_customuser_is_teamleader'),
    ]

    operations = [
        migrations.AddField(
            model_name='customuser',
            name='is_teammember',
            field=models.BooleanField(default=False),
        ),
    ]
