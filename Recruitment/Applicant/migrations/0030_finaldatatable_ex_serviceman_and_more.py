# Generated by Django 4.0.1 on 2022-11-24 12:43

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Applicant', '0029_otherdetail_ex_serviceman_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='finaldatatable',
            name='EX_SERVICEMAN',
            field=models.CharField(choices=[('YES', 'YES'), ('NO', 'NO')], max_length=3, null=True),
        ),
        migrations.AddField(
            model_name='finaldatatable',
            name='PERIOD_OF_SERVICE',
            field=models.PositiveIntegerField(blank=True, null=True),
        ),
    ]
