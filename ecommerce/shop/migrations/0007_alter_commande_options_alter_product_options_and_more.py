# Generated by Django 4.1.2 on 2023-09-25 17:09

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('shop', '0006_commande_order_id'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='commande',
            options={},
        ),
        migrations.AlterModelOptions(
            name='product',
            options={'ordering': ['-date_ajout']},
        ),
        migrations.RemoveField(
            model_name='commande',
            name='address',
        ),
        migrations.RemoveField(
            model_name='commande',
            name='email',
        ),
        migrations.RemoveField(
            model_name='commande',
            name='items',
        ),
        migrations.RemoveField(
            model_name='commande',
            name='nom',
        ),
        migrations.RemoveField(
            model_name='commande',
            name='order_id',
        ),
        migrations.RemoveField(
            model_name='commande',
            name='pays',
        ),
        migrations.RemoveField(
            model_name='commande',
            name='total',
        ),
        migrations.RemoveField(
            model_name='commande',
            name='ville',
        ),
        migrations.RemoveField(
            model_name='commande',
            name='zipcode',
        ),
        migrations.RemoveField(
            model_name='product',
            name='date_added',
        ),
        migrations.RemoveField(
            model_name='product',
            name='description',
        ),
        migrations.RemoveField(
            model_name='product',
            name='order_id',
        ),
        migrations.RemoveField(
            model_name='product',
            name='prix',
        ),
        migrations.RemoveField(
            model_name='product',
            name='title',
        ),
        migrations.AddField(
            model_name='category',
            name='description',
            field=models.TextField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='commande',
            name='complete',
            field=models.BooleanField(blank=True, default=False, null=True),
        ),
        migrations.AddField(
            model_name='commande',
            name='status',
            field=models.CharField(blank=True, max_length=200, null=True),
        ),
        migrations.AddField(
            model_name='commande',
            name='total_trans',
            field=models.DecimalField(blank=True, decimal_places=2, max_digits=10, null=True),
        ),
        migrations.AddField(
            model_name='commande',
            name='transaction_id',
            field=models.CharField(max_length=200, null=True),
        ),
        migrations.AddField(
            model_name='product',
            name='date_ajout',
            field=models.DateTimeField(default=django.utils.timezone.now),
        ),
        migrations.AddField(
            model_name='product',
            name='digital',
            field=models.BooleanField(blank=True, default=False, null=True),
        ),
        migrations.AddField(
            model_name='product',
            name='name',
            field=models.CharField(max_length=100, null=True),
        ),
        migrations.AddField(
            model_name='product',
            name='price',
            field=models.DecimalField(decimal_places=2, default=200, max_digits=10),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='category',
            name='name',
            field=models.CharField(blank=True, max_length=100, null=True),
        ),
        migrations.AlterField(
            model_name='commande',
            name='date_commande',
            field=models.DateTimeField(auto_now_add=True),
        ),
        migrations.AlterField(
            model_name='product',
            name='category',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='shop.category'),
        ),
        migrations.CreateModel(
            name='CommandeArticle',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('quantite', models.IntegerField(blank=True, default=0, null=True)),
                ('date_added', models.DateTimeField(auto_now_add=True)),
                ('commande', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='shop.commande')),
                ('product', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='shop.product')),
            ],
        ),
        migrations.CreateModel(
            name='Client',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100, null=True)),
                ('email', models.EmailField(max_length=200, null=True)),
                ('user', models.OneToOneField(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='client', to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='AddressChipping',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('addresse', models.CharField(max_length=100, null=True)),
                ('ville', models.CharField(max_length=100, null=True)),
                ('pays', models.CharField(max_length=200, null=True)),
                ('zipcode', models.CharField(max_length=100, null=True)),
                ('date_ajout', models.DateTimeField(auto_now_add=True)),
                ('client', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='shop.client')),
                ('commande', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='shop.commande')),
            ],
        ),
        migrations.AddField(
            model_name='commande',
            name='client',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='shop.client'),
        ),
    ]
