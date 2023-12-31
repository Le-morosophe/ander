# Generated by Django 4.1.2 on 2023-10-01 16:13

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('shop', '0011_laptop_smartphone_vehicule'),
    ]

    operations = [
        migrations.CreateModel(
            name='Message',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('email', models.EmailField(max_length=200)),
                ('message', models.TextField()),
            ],
        ),
        migrations.AddField(
            model_name='category',
            name='slug',
            field=models.SlugField(blank=True, null=True, unique=True),
        ),
    ]
