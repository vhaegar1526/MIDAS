# Generated by Django 3.2.7 on 2022-04-27 21:53

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0007_auto_20220427_2149'),
    ]

    operations = [
        migrations.AlterField(
            model_name='internationaladvisorycommittee',
            name='committee',
            field=models.ManyToManyField(blank=True, null=True, related_name='international_adviseries', to='core.StakeHolder'),
        ),
        migrations.AlterField(
            model_name='technicalprogramcommittee',
            name='committee',
            field=models.ManyToManyField(blank=True, null=True, related_name='technical_committee_members', to='core.StakeHolder'),
        ),
    ]
