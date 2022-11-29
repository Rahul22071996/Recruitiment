# Generated by Django 4.0.1 on 2022-08-08 11:23

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('Applicant', '0005_addressdetail_present_address'),
    ]

    operations = [
        migrations.CreateModel(
            name='BankDetail',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('BANK_NAME', models.CharField(blank=True, max_length=255, null=True)),
                ('IFSC_CODE', models.CharField(blank=True, max_length=255, null=True)),
                ('BRANCH_NAME', models.CharField(blank=True, max_length=255, null=True)),
                ('BRANCH_CODE', models.CharField(blank=True, max_length=255, null=True)),
                ('ACCOUNT_HOLDER_NAME', models.CharField(blank=True, max_length=255, null=True)),
                ('ACCOUNT_NUMBER', models.CharField(blank=True, max_length=255, null=True)),
                ('USER_CODE', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]