# Generated by Django 4.2.3 on 2023-07-13 15:04

import apps.accounts.utils
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Account',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('password', models.CharField(max_length=128, verbose_name='password')),
                ('last_login', models.DateTimeField(blank=True, null=True, verbose_name='last login')),
                ('email', models.EmailField(max_length=221, unique=True)),
                ('first_name', models.CharField(max_length=221, null=True)),
                ('last_name', models.CharField(max_length=221, null=True)),
                ('avatar', models.ImageField(blank=True, null=True, upload_to=apps.accounts.utils.avatar_path)),
                ('is_superuser', models.BooleanField(default=False)),
                ('is_staff', models.BooleanField(default=False)),
                ('is_active', models.BooleanField(default=True)),
                ('role', models.IntegerField(choices=[(0, 'Staff'), (1, 'Candidate'), (2, 'Recruiter')])),
                ('cv', models.FileField(blank=True, null=True, upload_to=apps.accounts.utils.cv_path)),
                ('modified_date', models.DateTimeField(auto_now=True)),
                ('created_date', models.DateTimeField(auto_now_add=True)),
            ],
            options={
                'abstract': False,
            },
        ),
    ]
