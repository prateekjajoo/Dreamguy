# Generated by Django 3.1.5 on 2021-04-03 16:42

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('payroll', '0002_auto_20210403_2019'),
    ]

    operations = [
        migrations.AddField(
            model_name='salary',
            name='net_salary',
            field=models.FloatField(default=0),
            preserve_default=False,
        ),
    ]
