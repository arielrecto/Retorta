# Generated by Django 4.2.6 on 2024-01-29 17:05

import django.core.validators
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Inbox',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50, null=True)),
                ('email', models.CharField(max_length=20, null=True)),
                ('message', models.TextField(max_length=255, null=True)),
                ('created_at', models.DateField(auto_now_add=True)),
                ('updated_at', models.DateField(auto_now=True)),
            ],
        ),
        migrations.CreateModel(
            name='Project',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('image', models.ImageField(null=True, upload_to='image')),
                ('name', models.CharField(max_length=20, null=True)),
                ('price', models.PositiveIntegerField(null=True, validators=[django.core.validators.MaxValueValidator(9999999999)])),
                ('description', models.TextField(max_length=255, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='Appointment',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('email', models.CharField(max_length=20, null=True)),
                ('name', models.CharField(max_length=50, null=True)),
                ('date', models.DateField(null=True)),
                ('contact_number', models.PositiveIntegerField(null=True, validators=[django.core.validators.MaxValueValidator(11)])),
                ('status', models.CharField(default='PENDING', max_length=20, null=True)),
                ('created_at', models.DateField(auto_now_add=True)),
                ('updated_at', models.DateField(auto_now=True)),
                ('project_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='housedesignapp.project')),
            ],
        ),
    ]
