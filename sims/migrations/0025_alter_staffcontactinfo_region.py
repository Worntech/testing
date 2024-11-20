# Generated by Django 4.2.11 on 2024-04-04 11:17

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('sims', '0024_auto_20240404_1119'),
    ]

    operations = [
        migrations.AlterField(
            model_name='staffcontactinfo',
            name='Region',
            field=models.CharField(choices=[('Arusha', 'Arusha'), ('Dodoma', 'Dodoma'), ('Mwanza', 'Mwanza'), ('Iringa', 'Iringa'), ('Tabora', 'Tabora'), ('Mara', 'Mara'), ('Kagera', 'Kagera'), ('Simiyu', 'Simiyu'), ('Shinyanga', 'Shinyanga'), ('Geita', 'Geita'), ('Kigoma', 'Kigoma'), ('Tabora', 'Tabora'), ('Manyara', 'Manyara'), ('Kilimanjaro', 'Kilimanjaro'), ('Katavi', 'Katavi'), ('Singida', 'Singida'), ('Tanga', 'Tanga'), ('Morogoro', 'Morogoro'), ('Pwani', 'Pwani'), ('Rukwa', 'Rukwa'), ('Mbeya', 'Mbeya'), ('Songwe', 'Songwe'), ('Njombe', 'Njombe'), ('Ruvuma', 'Ruvuma'), ('Mtwara', 'Mtwara'), ('Lindi', 'Lindi'), ('Songwe', 'Songwe')], max_length=40),
        ),
    ]