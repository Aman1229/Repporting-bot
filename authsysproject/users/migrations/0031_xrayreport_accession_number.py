# Generated by Django 5.0.1 on 2024-06-20 04:58

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0030_client_location_alter_client_email_alter_client_name_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='xrayreport',
            name='accession_number',
            field=models.CharField(blank=True, max_length=20, null=True),
        ),
    ]
