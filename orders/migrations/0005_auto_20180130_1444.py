# Generated by Django 2.0.1 on 2018-01-30 14:44

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('orders', '0004_auto_20180130_1348'),
    ]

    operations = [
        migrations.AlterField(
            model_name='productinorder',
            name='is_active',
            field=models.BooleanField(default=True),
        ),
    ]