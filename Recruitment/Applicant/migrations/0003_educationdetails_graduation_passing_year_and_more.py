# Generated by Django 4.0.1 on 2022-08-08 08:10

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('Applicant', '0002_educationdetails_otherdetail'),
    ]

    operations = [
        migrations.AddField(
            model_name='educationdetails',
            name='GRADUATION_PASSING_YEAR',
            field=models.CharField(blank=True, max_length=15, null=True),
        ),
        migrations.AddField(
            model_name='educationdetails',
            name='GRADUATION_PERCENTAGE',
            field=models.CharField(blank=True, max_length=15, null=True),
        ),
        migrations.AddField(
            model_name='educationdetails',
            name='GRADUATION_SUBJECT',
            field=models.CharField(blank=True, max_length=15, null=True),
        ),
        migrations.AddField(
            model_name='educationdetails',
            name='HSC_PASSING_YEAR',
            field=models.CharField(blank=True, max_length=15, null=True),
        ),
        migrations.AddField(
            model_name='educationdetails',
            name='HSC_PERCENTAGE',
            field=models.CharField(blank=True, max_length=15, null=True),
        ),
        migrations.AddField(
            model_name='educationdetails',
            name='HSC_SUBJECT',
            field=models.CharField(blank=True, max_length=15, null=True),
        ),
        migrations.AddField(
            model_name='educationdetails',
            name='HSSC_PASSING_YEAR',
            field=models.CharField(blank=True, max_length=15, null=True),
        ),
        migrations.AddField(
            model_name='educationdetails',
            name='HSSC_PERCENTAGE',
            field=models.CharField(blank=True, max_length=15, null=True),
        ),
        migrations.AddField(
            model_name='educationdetails',
            name='HSSC_SUBJECT',
            field=models.CharField(blank=True, max_length=15, null=True),
        ),
        migrations.AddField(
            model_name='educationdetails',
            name='POST_GRADUATION_PERCENTAGE',
            field=models.CharField(blank=True, max_length=15, null=True),
        ),
        migrations.AddField(
            model_name='educationdetails',
            name='POST_GRADUATION_SUBJECT',
            field=models.CharField(blank=True, max_length=15, null=True),
        ),
        migrations.AddField(
            model_name='educationdetails',
            name='POST_PASSING_YEAR',
            field=models.CharField(blank=True, max_length=15, null=True),
        ),
        migrations.AddField(
            model_name='educationdetails',
            name='USER_CODE',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL),
        ),
    ]
