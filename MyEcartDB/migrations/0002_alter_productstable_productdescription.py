# Generated by Django 4.2.10 on 2024-02-16 03:55

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('MyEcartDB', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='productstable',
            name='productDescription',
            field=models.TextField(null=True),
        ),
    ]