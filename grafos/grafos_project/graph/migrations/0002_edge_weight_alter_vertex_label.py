# Generated by Django 4.0.3 on 2022-04-05 21:08

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('graph', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='edge',
            name='weight',
            field=models.IntegerField(default=1),
        ),
        migrations.AlterField(
            model_name='vertex',
            name='label',
            field=models.CharField(max_length=30, unique=True),
        ),
    ]
