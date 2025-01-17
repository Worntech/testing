# Generated by Django 4.2.3 on 2024-03-22 09:56

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('sims', '0019_rename_nhif_number_patient_cost'),
    ]

    operations = [
        migrations.CreateModel(
            name='VITREOUSR',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('date_created', models.DateTimeField(auto_now_add=True)),
                ('Stutus', models.TextField()),
                ('Comment', models.TextField()),
                ('Title', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='sims.patient')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='VITREOUSL',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('date_created', models.DateTimeField(auto_now_add=True)),
                ('Stutus', models.TextField()),
                ('Comment', models.TextField()),
                ('Title', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='sims.patient')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='RETINAR',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('date_created', models.DateTimeField(auto_now_add=True)),
                ('Stutus', models.TextField()),
                ('Comment', models.TextField()),
                ('Title', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='sims.patient')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='RETINAL',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('date_created', models.DateTimeField(auto_now_add=True)),
                ('Stutus', models.TextField()),
                ('Comment', models.TextField()),
                ('Title', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='sims.patient')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='PUPILR',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('date_created', models.DateTimeField(auto_now_add=True)),
                ('Stutus', models.TextField()),
                ('Comment', models.TextField()),
                ('Title', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='sims.patient')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='PUPILL',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('date_created', models.DateTimeField(auto_now_add=True)),
                ('Stutus', models.TextField()),
                ('Comment', models.TextField()),
                ('Title', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='sims.patient')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='LENSR',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('date_created', models.DateTimeField(auto_now_add=True)),
                ('Stutus', models.TextField()),
                ('Comment', models.TextField()),
                ('Title', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='sims.patient')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='LENSL',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('date_created', models.DateTimeField(auto_now_add=True)),
                ('Stutus', models.TextField()),
                ('Comment', models.TextField()),
                ('Title', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='sims.patient')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='IRISR',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('date_created', models.DateTimeField(auto_now_add=True)),
                ('Stutus', models.TextField()),
                ('Comment', models.TextField()),
                ('Title', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='sims.patient')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='IRISL',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('date_created', models.DateTimeField(auto_now_add=True)),
                ('Stutus', models.TextField()),
                ('Comment', models.TextField()),
                ('Title', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='sims.patient')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='EYELIDR',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('date_created', models.DateTimeField(auto_now_add=True)),
                ('Stutus', models.TextField()),
                ('Comment', models.TextField()),
                ('Title', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='sims.patient')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='EYELIDL',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('date_created', models.DateTimeField(auto_now_add=True)),
                ('Stutus', models.TextField()),
                ('Comment', models.TextField()),
                ('Title', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='sims.patient')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='CORNEAR',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('date_created', models.DateTimeField(auto_now_add=True)),
                ('Stutus', models.TextField()),
                ('Comment', models.TextField()),
                ('Title', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='sims.patient')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='CORNEAL',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('date_created', models.DateTimeField(auto_now_add=True)),
                ('Stutus', models.TextField()),
                ('Comment', models.TextField()),
                ('Title', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='sims.patient')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='CONJUNCTIVAR',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('date_created', models.DateTimeField(auto_now_add=True)),
                ('Stutus', models.TextField()),
                ('Comment', models.TextField()),
                ('Title', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='sims.patient')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='CONJUNCTIVAL',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('date_created', models.DateTimeField(auto_now_add=True)),
                ('Stutus', models.TextField()),
                ('Comment', models.TextField()),
                ('Title', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='sims.patient')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='ACR',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('date_created', models.DateTimeField(auto_now_add=True)),
                ('Stutus', models.TextField()),
                ('Comment', models.TextField()),
                ('Title', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='sims.patient')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='ACL',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('date_created', models.DateTimeField(auto_now_add=True)),
                ('Stutus', models.TextField()),
                ('Comment', models.TextField()),
                ('Title', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='sims.patient')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
