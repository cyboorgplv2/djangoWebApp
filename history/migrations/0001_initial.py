# Generated by Django 4.0.1 on 2022-01-15 18:56

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='History',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('description', models.TextField()),
                ('product_name', models.TextField()),
                ('update_date', models.DateTimeField(verbose_name='modification date')),
            ],
        ),
    ]
