# Generated by Django 4.2.5 on 2023-10-16 00:00

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('myapp', '0003_produit'),
    ]

    operations = [
        migrations.AlterField(
            model_name='produit',
            name='price',
            field=models.DecimalField(decimal_places=2, max_digits=3, null=True),
        ),
    ]
