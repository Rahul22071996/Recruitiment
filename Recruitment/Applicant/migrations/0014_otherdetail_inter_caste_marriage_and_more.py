# Generated by Django 4.0.1 on 2022-08-23 12:12

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Applicant', '0013_remove_personaldetail_candidate_is_a_widow_divorced_abandoned_woman_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='otherdetail',
            name='INTER_CASTE_MARRIAGE',
            field=models.CharField(choices=[('YES', 'YES'), ('NO', 'NO')], max_length=3, null=True),
        ),
        migrations.AddField(
            model_name='otherdetail',
            name='VIKRAM_AWARDEE_SPORTSPERSON',
            field=models.CharField(choices=[('YES', 'YES'), ('NO', 'NO')], max_length=3, null=True),
        ),
    ]
