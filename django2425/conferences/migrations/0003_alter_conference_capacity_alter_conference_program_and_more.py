# Generated by Django 4.2 on 2024-10-10 20:35

import datetime
import django.core.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('conferences', '0002_alter_conference_category'),
    ]

    operations = [
        migrations.AlterField(
            model_name='conference',
            name='capacity',
            field=models.IntegerField(validators=[django.core.validators.MaxValueValidator(limit_value=900, message='capacity must be under 900')]),
        ),
        migrations.AlterField(
            model_name='conference',
            name='program',
            field=models.FileField(upload_to='files/', validators=[django.core.validators.FileExtensionValidator(allowed_extensions=['pdf', 'png', 'jpeg', 'jpg'], message='only pdf,png,jpg,jpeg are allowed')]),
        ),
        migrations.AlterField(
            model_name='conference',
            name='start_date',
            field=models.DateField(default=datetime.date(2024, 10, 10)),
        ),
        migrations.AddConstraint(
            model_name='conference',
            constraint=models.CheckConstraint(check=models.Q(('start_date__gte', datetime.date(2024, 10, 10))), name='the start date must be greater than today or equal'),
        ),
    ]
