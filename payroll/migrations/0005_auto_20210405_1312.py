# Generated by Django 3.1.5 on 2021-04-05 07:42

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('payroll', '0004_auto_20210405_1253'),
    ]

    operations = [
        migrations.AlterField(
            model_name='employee',
            name='gender',
            field=models.CharField(blank=True, choices=[('Male', 'Male'), ('Female', 'Female')], default='None', max_length=15, null=True),
        ),
    ]
