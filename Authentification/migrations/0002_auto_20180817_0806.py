# Generated by Django 2.0.7 on 2018-08-17 08:06

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('Authentification', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='users',
            name='professor',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='Authentification.UserP'),
        ),
    ]