# Generated by Django 4.2.3 on 2024-03-13 11:23

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('sims', '0008_rename_clinic_clinic_clinics'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='Clinic',
            new_name='Clinics',
        ),
    ]