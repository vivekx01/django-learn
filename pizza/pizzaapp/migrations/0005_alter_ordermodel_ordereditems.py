# Generated by Django 3.2 on 2021-05-03 07:21

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('pizzaapp', '0004_rename_email_ordermodel_phone'),
    ]

    operations = [
        migrations.AlterField(
            model_name='ordermodel',
            name='ordereditems',
            field=models.CharField(max_length=50),
        ),
    ]
