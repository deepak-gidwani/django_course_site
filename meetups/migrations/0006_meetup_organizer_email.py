# Generated by Django 4.0.1 on 2023-03-20 13:47

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('meetups', '0005_participant_meetup_participants'),
    ]

    operations = [
        migrations.AddField(
            model_name='meetup',
            name='organizer_email',
            field=models.EmailField(max_length=254, null=True),
        ),
    ]