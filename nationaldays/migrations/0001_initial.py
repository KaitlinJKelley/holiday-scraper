# Generated by Django 3.2.5 on 2021-08-17 00:15

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Day',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('date', models.DateField()),
                ('name', models.CharField(max_length=250)),
                ('day_history', models.TextField(null=True)),
                ('day_about', models.TextField(null=True)),
            ],
        ),
    ]
