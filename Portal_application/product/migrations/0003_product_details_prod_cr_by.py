# Generated by Django 3.0.2 on 2020-04-15 08:47

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('product', '0002_auto_20200409_2332'),
    ]

    operations = [
        migrations.AddField(
            model_name='product_details',
            name='prod_cr_by',
            field=models.CharField(default='abhay', max_length=100),
            preserve_default=False,
        ),
    ]
