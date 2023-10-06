# Generated by Django 4.1.2 on 2023-09-27 05:50

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('shop', '0010_product_description_alter_product_image'),
    ]

    operations = [
        migrations.CreateModel(
            name='Laptop',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100, null=True)),
                ('price', models.DecimalField(decimal_places=2, max_digits=10)),
                ('digital', models.BooleanField(blank=True, default=False, null=True)),
                ('image', models.CharField(max_length=500)),
                ('description', models.TextField()),
                ('date_ajout', models.DateTimeField(default=django.utils.timezone.now)),
            ],
            options={
                'ordering': ['-date_ajout'],
            },
        ),
        migrations.CreateModel(
            name='Smartphone',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100, null=True)),
                ('price', models.DecimalField(decimal_places=2, max_digits=10)),
                ('digital', models.BooleanField(blank=True, default=False, null=True)),
                ('image', models.CharField(max_length=500)),
                ('description', models.TextField()),
                ('date_ajout', models.DateTimeField(default=django.utils.timezone.now)),
            ],
            options={
                'ordering': ['-date_ajout'],
            },
        ),
        migrations.CreateModel(
            name='Vehicule',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100, null=True)),
                ('price', models.DecimalField(decimal_places=2, max_digits=10)),
                ('digital', models.BooleanField(blank=True, default=False, null=True)),
                ('image', models.CharField(max_length=500)),
                ('description', models.TextField()),
                ('date_ajout', models.DateTimeField(default=django.utils.timezone.now)),
            ],
            options={
                'ordering': ['-date_ajout'],
            },
        ),
    ]
