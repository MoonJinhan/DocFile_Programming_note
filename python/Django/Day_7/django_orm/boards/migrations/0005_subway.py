# Generated by Django 2.2.7 on 2019-11-14 08:22

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('boards', '0004_delete_subway'),
    ]

    operations = [
        migrations.CreateModel(
            name='Subway',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=10)),
                ('date', models.DateField()),
                ('sandwitch', models.CharField(max_length=15)),
                ('size', models.IntegerField()),
                ('bread', models.CharField(max_length=15)),
                ('source', models.CharField(max_length=10)),
            ],
        ),
    ]