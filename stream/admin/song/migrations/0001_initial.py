# Generated by Django 5.0.3 on 2024-03-19 14:25

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('artist', '0001_initial'),
        ('genre', '0001_initial'),
        ('mood', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Song',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('song_name', models.CharField(max_length=50)),
                ('song_des', models.CharField(default='This is a Popular Song!', max_length=150)),
                ('song_length', models.CharField(max_length=10)),
                ('song_file', models.FileField(upload_to='songs/')),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('artist_name', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='artist.artist')),
                ('genre_name', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='genre.genre')),
                ('mood_name', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='mood.mood')),
            ],
        ),
    ]
