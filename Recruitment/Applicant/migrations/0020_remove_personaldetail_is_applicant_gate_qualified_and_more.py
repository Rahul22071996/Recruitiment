# Generated by Django 4.0.1 on 2022-11-18 10:09

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Applicant', '0019_flagdetail'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='personaldetail',
            name='IS_APPLICANT_GATE_QUALIFIED',
        ),
        migrations.AddField(
            model_name='personaldetail',
            name='EMPLOYMENT_TYPE',
            field=models.CharField(blank=True, choices=[('Regular', 'Regular'), ('Contractual', 'Contractual')], max_length=255, null=True),
        ),
    ]