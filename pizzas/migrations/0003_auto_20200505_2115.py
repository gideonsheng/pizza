# Generated by Django 3.0.5 on 2020-05-06 02:15

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('pizzas', '0002_auto_20200505_2111'),
    ]

    operations = [
        migrations.AlterField(
            model_name='topping',
            name='text',
            field=models.CharField(max_length=200),
        ),
    ]