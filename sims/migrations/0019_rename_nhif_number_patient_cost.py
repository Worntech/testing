# Generated by Django 4.2.3 on 2024-03-21 13:18

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('sims', '0018_alter_mystaff_is_admin_alter_mystaff_is_staff'),
    ]

    operations = [
        migrations.RenameField(
            model_name='patient',
            old_name='NHIF_Number',
            new_name='Cost',
        ),
    ]