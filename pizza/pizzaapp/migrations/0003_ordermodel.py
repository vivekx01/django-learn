# Generated by Django 3.2 on 2021-05-03 06:15

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('pizzaapp', '0002_alter_pizzamodel_name'),
    ]

    operations = [
        migrations.CreateModel(
            name='OrderModel',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('username', models.CharField(max_length=20)),
                ('email', models.CharField(max_length=20)),
                ('address', models.CharField(max_length=20)),
                ('ordereditems', models.CharField(max_length=20)),
            ],
        ),
    ]
