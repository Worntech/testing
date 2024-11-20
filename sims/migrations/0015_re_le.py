# Generated by Django 4.2.3 on 2024-03-21 11:52

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('sims', '0014_investigation'),
    ]

    operations = [
        migrations.CreateModel(
            name='RE',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('date_created', models.DateTimeField(auto_now_add=True)),
                ('RE', models.TextField()),
                ('PH', models.TextField()),
                ('Title', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='sims.patient')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='LE',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('date_created', models.DateTimeField(auto_now_add=True)),
                ('LE', models.TextField()),
                ('PH', models.TextField()),
                ('Title', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='sims.patient')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]