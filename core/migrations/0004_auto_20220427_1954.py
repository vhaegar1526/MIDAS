# Generated by Django 3.2.7 on 2022-04-27 19:54

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0003_auto_20220426_1158'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='bulletpoint',
            name='conference',
        ),
        migrations.RemoveField(
            model_name='publicationpartner',
            name='conference',
        ),
        migrations.RemoveField(
            model_name='scheduleforearlytrack',
            name='conference',
        ),
        migrations.RemoveField(
            model_name='scheduleforregulartrack',
            name='conference',
        ),
        migrations.RemoveField(
            model_name='speaker',
            name='conference',
        ),
        migrations.RemoveField(
            model_name='steeringcommittee',
            name='advisory_chair',
        ),
        migrations.RemoveField(
            model_name='steeringcommittee',
            name='chief_patron',
        ),
        migrations.RemoveField(
            model_name='steeringcommittee',
            name='co_convener',
        ),
        migrations.RemoveField(
            model_name='steeringcommittee',
            name='co_patron',
        ),
        migrations.RemoveField(
            model_name='steeringcommittee',
            name='conference',
        ),
        migrations.RemoveField(
            model_name='steeringcommittee',
            name='conference_chair',
        ),
        migrations.RemoveField(
            model_name='steeringcommittee',
            name='convener',
        ),
        migrations.RemoveField(
            model_name='steeringcommittee',
            name='corporate_chair',
        ),
        migrations.RemoveField(
            model_name='steeringcommittee',
            name='editorial_board',
        ),
        migrations.RemoveField(
            model_name='steeringcommittee',
            name='general_chair',
        ),
        migrations.RemoveField(
            model_name='steeringcommittee',
            name='general_co_chair',
        ),
        migrations.RemoveField(
            model_name='steeringcommittee',
            name='honorary_chair',
        ),
        migrations.RemoveField(
            model_name='steeringcommittee',
            name='patron',
        ),
        migrations.RemoveField(
            model_name='steeringcommittee',
            name='publicity_chair',
        ),
        migrations.RemoveField(
            model_name='steeringcommittee',
            name='special_session_chair',
        ),
        migrations.RemoveField(
            model_name='steeringcommittee',
            name='tpc_chair',
        ),
        migrations.RemoveField(
            model_name='steeringcommittee',
            name='tpc_co_chair',
        ),
        migrations.RemoveField(
            model_name='steeringcommittee',
            name='track_chair',
        ),
        migrations.RemoveField(
            model_name='technicalpartner',
            name='conference',
        ),
        migrations.RemoveField(
            model_name='trackforpaper',
            name='conference',
        ),
        migrations.RemoveField(
            model_name='venue',
            name='conference',
        ),
        migrations.DeleteModel(
            name='Announcement',
        ),
        migrations.DeleteModel(
            name='BulletPoint',
        ),
        migrations.DeleteModel(
            name='PublicationPartner',
        ),
        migrations.DeleteModel(
            name='ScheduleForEarlyTrack',
        ),
        migrations.DeleteModel(
            name='ScheduleForRegularTrack',
        ),
        migrations.DeleteModel(
            name='Speaker',
        ),
        migrations.DeleteModel(
            name='StakeHolder',
        ),
        migrations.DeleteModel(
            name='SteeringCommittee',
        ),
        migrations.DeleteModel(
            name='TechnicalPartner',
        ),
        migrations.DeleteModel(
            name='TrackForPaper',
        ),
        migrations.DeleteModel(
            name='Venue',
        ),
    ]
