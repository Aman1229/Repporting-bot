# Generated by Django 5.0.1 on 2024-02-27 09:35

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0002_remove_dicomdata_radiologist_dicomdata_radiologists'),
    ]

    operations = [
        migrations.RenameField(
            model_name='dicomdata',
            old_name='radiologists',
            new_name='radiologist',
        ),
    ]
