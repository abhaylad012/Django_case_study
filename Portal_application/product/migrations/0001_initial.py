# Generated by Django 3.0.2 on 2020-04-07 10:41

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='product_details',
            fields=[
                ('prod_id', models.AutoField(primary_key=True, serialize=False)),
                ('prod_name', models.CharField(max_length=100)),
                ('prod_desc', models.CharField(max_length=1000)),
                ('prod_topic', models.CharField(max_length=100)),
                ('prod_logo', models.ImageField(upload_to='logos')),
            ],
        ),
    ]
