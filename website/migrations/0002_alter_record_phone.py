# Generated by Django 5.0 on 2023-12-13 10:48

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('website', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='record',
            name='phone',
            field=models.CharField(max_length=15),
        ),
    ]