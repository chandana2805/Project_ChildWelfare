# Generated by Django 3.1.7 on 2021-05-13 12:07

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('App', '0002_orgdetails_no_of_childrens'),
    ]

    operations = [
        migrations.AlterField(
            model_name='user',
            name='first_name',
            field=models.CharField(blank=True, max_length=150, verbose_name='first name'),
        ),
    ]
