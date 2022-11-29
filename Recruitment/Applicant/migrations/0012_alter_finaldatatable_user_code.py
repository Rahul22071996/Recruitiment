# Generated by Django 4.0.1 on 2022-08-18 11:39

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('Applicant', '0011_alter_finaldatatable_user_code'),
    ]

    operations = [
        migrations.AlterField(
            model_name='finaldatatable',
            name='USER_CODE',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL),
        ),
    ]
