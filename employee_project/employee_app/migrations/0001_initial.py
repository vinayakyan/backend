# Generated by Django 5.0.2 on 2024-02-15 10:47

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Employee',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=30)),
                ('salary', models.FloatField()),
                ('company', models.CharField(max_length=50)),
                ('designation', models.CharField(max_length=30)),
            ],
        ),
    ]
