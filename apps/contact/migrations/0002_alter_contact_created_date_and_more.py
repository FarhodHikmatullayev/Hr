# Generated by Django 4.2.3 on 2023-07-12 11:50

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('contact', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='contact',
            name='created_date',
            field=models.DateTimeField(auto_now_add=True, null=True),
        ),
        migrations.AlterField(
            model_name='contact',
            name='modified_date',
            field=models.DateTimeField(auto_now=True, null=True),
        ),
    ]