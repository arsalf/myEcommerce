# Generated by Django 3.2.4 on 2021-11-13 12:42

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='product',
            fields=[
                ('id', models.IntegerField(primary_key=True, serialize=False)),
                ('name', models.CharField(max_length=100)),
                ('image', models.CharField(max_length=255)),
                ('price', models.IntegerField()),
            ],
        ),
    ]
