# Generated by Django 2.0.7 on 2018-08-24 18:03

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('exam', '0002_exam_mode'),
    ]

    operations = [
        migrations.AlterField(
            model_name='exam',
            name='mode',
            field=models.CharField(blank=True, choices=[('TT', 'Training_Timer'), ('T', 'Training'), ('OC', 'One_try_certifie'), ('O', 'One_try')], max_length=1, null=True),
        ),
    ]
