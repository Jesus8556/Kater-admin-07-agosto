# Generated by Django 3.2 on 2023-08-02 15:31

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('dashboard', '0002_alter_manodeobra_precio_unitario'),
    ]

    operations = [
        migrations.AlterField(
            model_name='consultoria',
            name='precio_unitario',
            field=models.DecimalField(blank=True, decimal_places=2, default=0, max_digits=10),
        ),
        migrations.AlterField(
            model_name='piezasrepuesto',
            name='precio_unitario',
            field=models.DecimalField(blank=True, decimal_places=2, default=0, max_digits=10),
        ),
    ]