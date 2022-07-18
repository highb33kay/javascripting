# Generated by Django 4.0.4 on 2022-07-18 03:34

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('scores', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='game',
            name='wins',
            field=models.IntegerField(default=0, verbose_name='wins'),
        ),
        migrations.AlterField(
            model_name='game',
            name='loss',
            field=models.IntegerField(default=0, verbose_name='loss'),
        ),
        migrations.AlterField(
            model_name='game',
            name='points',
            field=models.IntegerField(default=0, verbose_name='points'),
        ),
    ]
