# Generated by Django 2.0.7 on 2018-08-17 09:19

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Authentification', '0004_auto_20180817_0910'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='users',
            name='professor',
        ),
        migrations.AddField(
            model_name='users',
            name='professor',
            field=models.ManyToManyField(to='Authentification.UserP'),
        ),
    ]
