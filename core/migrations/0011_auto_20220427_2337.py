# Generated by Django 3.2.7 on 2022-04-27 23:37

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0010_announcement_bulletpoint_internationaladvisorycommittee_nationaladvisorycommittee_organisingcommitte'),
    ]

    operations = [
        migrations.AlterField(
            model_name='internationaladvisorycommittee',
            name='committee',
            field=models.ManyToManyField(blank=True, null=True, related_name='international_members', to='core.StakeHolder'),
        ),
        migrations.AlterField(
            model_name='internationaladvisorycommittee',
            name='conference',
            field=models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, related_name='international_advisory', to='core.conference'),
        ),
        migrations.AlterField(
            model_name='nationaladvisorycommittee',
            name='committee',
            field=models.ManyToManyField(blank=True, null=True, related_name='national_members', to='core.StakeHolder'),
        ),
        migrations.AlterField(
            model_name='nationaladvisorycommittee',
            name='conference',
            field=models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, related_name='national_advisory', to='core.conference'),
        ),
        migrations.AlterField(
            model_name='technicalprogramcommittee',
            name='committee',
            field=models.ManyToManyField(blank=True, null=True, related_name='tpc_members', to='core.StakeHolder'),
        ),
        migrations.AlterField(
            model_name='technicalprogramcommittee',
            name='conference',
            field=models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, related_name='technical_program', to='core.conference'),
        ),
    ]
