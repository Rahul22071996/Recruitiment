# Generated by Django 4.0.1 on 2022-11-18 10:14

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Applicant', '0020_remove_personaldetail_is_applicant_gate_qualified_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='personaldetail',
            name='DATE_OF_BIRTH',
            field=models.DateField(default='2000-01-01'),
        ),
    ]