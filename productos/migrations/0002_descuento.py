# Generated by Django 3.2.2 on 2021-05-19 21:31

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('productos', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Descuento',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('codigo', models.CharField(max_length=12)),
                ('descripcion', models.CharField(max_length=255)),
                ('descuento', models.FloatField()),
            ],
        ),
    ]
