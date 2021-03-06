# Generated by Django 3.2.7 on 2022-04-26 09:26

from django.db import migrations, models
import django.db.models.deletion
import django_better_admin_arrayfield.models.fields


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='StakeHolder',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('full_name', models.CharField(max_length=100)),
                ('afiliation', models.CharField(max_length=250)),
                ('website', models.URLField(blank=True)),
            ],
            options={
                'ordering': ['created_at'],
            },
        ),
        migrations.CreateModel(
            name='Venue',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('university', models.CharField(max_length=100)),
                ('home_city', models.CharField(blank=True, max_length=50)),
                ('home_state', models.CharField(blank=True, max_length=50)),
                ('home_country', models.CharField(max_length=50)),
                ('start_date', models.DateField()),
                ('end_date', models.DateField()),
                ('website_url', models.URLField(default='/')),
                ('cover_image', models.FileField(upload_to='')),
                ('university_logo', models.FileField(upload_to='')),
                ('university_description', models.TextField(max_length=350)),
                ('conference', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, related_name='venue', to='core.conference')),
            ],
            options={
                'ordering': ['created_at'],
            },
        ),
        migrations.CreateModel(
            name='TrackForPaper',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('title', models.CharField(max_length=75)),
                ('pointers', django_better_admin_arrayfield.models.fields.ArrayField(base_field=models.CharField(default='', max_length=250), blank=True, null=True, size=None)),
                ('conference', models.ForeignKey(default=None, on_delete=django.db.models.deletion.CASCADE, related_name='tracks', to='core.conference')),
            ],
            options={
                'ordering': ['created_at'],
            },
        ),
        migrations.CreateModel(
            name='TechnicalPartner',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('org_name', models.CharField(max_length=50)),
                ('website', models.URLField(blank=True)),
                ('logo', models.FileField(upload_to='')),
                ('conference', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='technical_partners', to='core.conference')),
            ],
            options={
                'ordering': ['created_at'],
            },
        ),
        migrations.CreateModel(
            name='SteeringCommittee',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('full_name', models.CharField(max_length=100)),
                ('university', models.CharField(max_length=100)),
                ('home_location', models.CharField(max_length=100)),
                ('affiliation', models.CharField(max_length=100)),
                ('avatar_image', models.FileField(upload_to='')),
                ('website', models.URLField(blank=True)),
                ('chief_patron', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, related_name='chief_patron', to='core.stakeholder')),
                ('co_patron', models.ManyToManyField(related_name='co_patrons', to='core.StakeHolder')),
                ('conference', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to='core.conference')),
                ('patron', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, related_name='patron', to='core.stakeholder')),
            ],
        ),
        migrations.CreateModel(
            name='Speaker',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('full_name', models.CharField(max_length=100)),
                ('university', models.CharField(max_length=100)),
                ('home_location', models.CharField(max_length=100)),
                ('affiliation', models.CharField(max_length=100)),
                ('avatar_image', models.FileField(upload_to='')),
                ('website', models.URLField(blank=True)),
                ('conference', models.ForeignKey(default=None, on_delete=django.db.models.deletion.CASCADE, related_name='speakers', to='core.conference')),
            ],
            options={
                'ordering': ['created_at'],
            },
        ),
        migrations.CreateModel(
            name='ScheduleForRegularTrack',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('last_date', models.DateField()),
                ('author_notification', models.DateField()),
                ('registration_deadline', models.DateField()),
                ('conference_dates', models.DateField()),
                ('conference', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, related_name='early_regular_schedule', to='core.conference')),
            ],
            options={
                'ordering': ['created_at'],
            },
        ),
        migrations.CreateModel(
            name='ScheduleForEarlyTrack',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('last_date', models.DateField()),
                ('author_notification', models.DateField()),
                ('registration_deadline', models.DateField()),
                ('conference_dates', models.DateField()),
                ('conference', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, related_name='early_track_schedule', to='core.conference')),
            ],
            options={
                'ordering': ['created_at'],
            },
        ),
        migrations.CreateModel(
            name='PublicationPartner',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('org_name', models.CharField(max_length=50)),
                ('website', models.URLField(blank=True)),
                ('logo', models.FileField(upload_to='')),
                ('conference', models.ForeignKey(default=None, on_delete=django.db.models.deletion.CASCADE, related_name='publication_partners', to='core.conference')),
            ],
            options={
                'ordering': ['created_at'],
            },
        ),
        migrations.CreateModel(
            name='BulletPoint',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('title', models.CharField(max_length=50)),
                ('description', models.TextField(max_length=250)),
                ('avatar_image', models.FileField(upload_to='')),
                ('conference', models.ForeignKey(default=None, on_delete=django.db.models.deletion.CASCADE, related_name='bulletpoints', to='core.conference')),
            ],
            options={
                'ordering': ['created_at'],
            },
        ),
        migrations.CreateModel(
            name='Announcement',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('title', models.CharField(max_length=75)),
                ('url', models.URLField(blank=True)),
                ('description', models.TextField(blank=True, max_length=250)),
                ('conference', models.ForeignKey(default=None, on_delete=django.db.models.deletion.CASCADE, related_name='announcements', to='core.conference')),
            ],
            options={
                'ordering': ['created_at'],
            },
        ),
    ]
