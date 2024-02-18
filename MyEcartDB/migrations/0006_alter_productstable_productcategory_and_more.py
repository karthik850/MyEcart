# Generated by Django 4.2.10 on 2024-02-18 09:21

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('MyEcartDB', '0005_alter_productimagestable_productname'),
    ]

    operations = [
        migrations.AlterField(
            model_name='productstable',
            name='productCategory',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to='MyEcartDB.categorytable'),
        ),
        migrations.AlterField(
            model_name='specialofferstable',
            name='specialOffersCategory',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to='MyEcartDB.categorytable'),
        ),
    ]