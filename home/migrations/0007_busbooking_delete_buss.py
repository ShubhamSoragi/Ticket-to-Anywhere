# Generated by Django 5.0.4 on 2024-09-09 15:14

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0006_buss'),
    ]

    operations = [
        migrations.CreateModel(
            name='BusBooking',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('age', models.IntegerField()),
                ('bus_number', models.CharField(max_length=20)),
                ('seat_number', models.CharField(max_length=10)),
            ],
        ),
        migrations.DeleteModel(
            name='Buss',
        ),
    ]
