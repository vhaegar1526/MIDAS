# Generated by Django 3.2.7 on 2022-04-26 11:58

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0002_announcement_bulletpoint_publicationpartner_scheduleforearlytrack_scheduleforregulartrack_speaker_st'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='steeringcommittee',
            name='affiliation',
        ),
        migrations.RemoveField(
            model_name='steeringcommittee',
            name='avatar_image',
        ),
        migrations.RemoveField(
            model_name='steeringcommittee',
            name='full_name',
        ),
        migrations.RemoveField(
            model_name='steeringcommittee',
            name='home_location',
        ),
        migrations.RemoveField(
            model_name='steeringcommittee',
            name='university',
        ),
        migrations.RemoveField(
            model_name='steeringcommittee',
            name='website',
        ),
        migrations.AddField(
            model_name='steeringcommittee',
            name='advisory_chair',
            field=models.ManyToManyField(related_name='advisory_chairs', to='core.StakeHolder'),
        ),
        migrations.AddField(
            model_name='steeringcommittee',
            name='co_convener',
            field=models.ManyToManyField(related_name='co_conveners', to='core.StakeHolder'),
        ),
        migrations.AddField(
            model_name='steeringcommittee',
            name='conference_chair',
            field=models.ManyToManyField(related_name='conference_chairs', to='core.StakeHolder'),
        ),
        migrations.AddField(
            model_name='steeringcommittee',
            name='convener',
            field=models.ManyToManyField(related_name='convener', to='core.StakeHolder'),
        ),
        migrations.AddField(
            model_name='steeringcommittee',
            name='corporate_chair',
            field=models.ManyToManyField(related_name='corporate_chairs', to='core.StakeHolder'),
        ),
        migrations.AddField(
            model_name='steeringcommittee',
            name='editorial_board',
            field=models.ManyToManyField(related_name='editorial_boards', to='core.StakeHolder'),
        ),
        migrations.AddField(
            model_name='steeringcommittee',
            name='general_chair',
            field=models.ManyToManyField(related_name='general_chairs', to='core.StakeHolder'),
        ),
        migrations.AddField(
            model_name='steeringcommittee',
            name='general_co_chair',
            field=models.ManyToManyField(related_name='general_co_chairs', to='core.StakeHolder'),
        ),
        migrations.AddField(
            model_name='steeringcommittee',
            name='honorary_chair',
            field=models.ManyToManyField(related_name='honorary_chairs', to='core.StakeHolder'),
        ),
        migrations.AddField(
            model_name='steeringcommittee',
            name='publicity_chair',
            field=models.ManyToManyField(related_name='publicity_chairs', to='core.StakeHolder'),
        ),
        migrations.AddField(
            model_name='steeringcommittee',
            name='special_session_chair',
            field=models.ManyToManyField(related_name='special_session_chairs', to='core.StakeHolder'),
        ),
        migrations.AddField(
            model_name='steeringcommittee',
            name='tpc_chair',
            field=models.ManyToManyField(related_name='tpc_chairs', to='core.StakeHolder'),
        ),
        migrations.AddField(
            model_name='steeringcommittee',
            name='tpc_co_chair',
            field=models.ManyToManyField(related_name='tpc_co_chairs', to='core.StakeHolder'),
        ),
        migrations.AddField(
            model_name='steeringcommittee',
            name='track_chair',
            field=models.ManyToManyField(related_name='track_chairs', to='core.StakeHolder'),
        ),
    ]
