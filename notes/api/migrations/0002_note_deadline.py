# Generated by Django 4.2.7 on 2023-12-03 11:04

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='note',
            name='deadline',
            field=models.DateTimeField(null=True),
        ),
    ]
