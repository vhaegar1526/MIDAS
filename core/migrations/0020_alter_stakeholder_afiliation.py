# Generated by Django 3.2.7 on 2022-05-01 14:19

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0019_auto_20220501_1347'),
    ]

    operations = [
        migrations.AlterField(
            model_name='stakeholder',
            name='afiliation',
            field=models.CharField(blank=True, max_length=250, null=True),
        ),
    ]
