# Generated by Django 5.1.2 on 2024-11-19 12:03

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Bhuna2',
            fields=[
                ('empno', models.IntegerField(primary_key=True, serialize=False)),
                ('ename', models.CharField(max_length=20)),
                ('job', models.CharField(max_length=20)),
                ('sal', models.FloatField()),
            ],
        ),
    ]