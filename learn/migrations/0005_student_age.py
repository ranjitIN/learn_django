# Generated by Django 5.0.1 on 2024-02-04 06:04

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('learn', '0004_remove_student_age'),
    ]

    operations = [
        migrations.AddField(
            model_name='student',
            name='age',
            field=models.IntegerField(default=0),
        ),
    ]
