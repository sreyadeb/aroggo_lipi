# Generated by Django 3.2.9 on 2022-01-08 16:40

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('patients', '0005_auto_20220108_2237'),
    ]

    operations = [
        migrations.AlterField(
            model_name='chiefcomplain',
            name='visitingDate',
            field=models.DateField(),
        ),
        migrations.AlterField(
            model_name='currentstatus',
            name='visitingDate',
            field=models.DateField(),
        ),
        migrations.AlterField(
            model_name='diagnosis',
            name='visitingDate',
            field=models.DateField(),
        ),
        migrations.AlterField(
            model_name='instruction',
            name='visitingDate',
            field=models.DateField(),
        ),
        migrations.AlterField(
            model_name='medicine',
            name='visitingDate',
            field=models.DateField(),
        ),
    ]
