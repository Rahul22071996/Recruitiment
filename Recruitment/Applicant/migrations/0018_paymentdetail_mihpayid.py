# Generated by Django 4.0.1 on 2022-09-24 18:43

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Applicant', '0017_paymentdetail_user'),
    ]

    operations = [
        migrations.AddField(
            model_name='paymentdetail',
            name='mihpayid',
            field=models.CharField(blank=True, max_length=100, null=True),
        ),
    ]
