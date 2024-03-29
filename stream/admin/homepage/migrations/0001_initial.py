# Generated by Django 5.0.3 on 2024-03-19 14:25

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('song', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Homepage',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(blank=True, default=None, max_length=150)),
                ('artist', models.CharField(blank=True, default=None, max_length=150)),
                ('created_at', models.DateTimeField(auto_now_add=True, null=True)),
                ('updated_at', models.DateTimeField(auto_now=True, null=True)),
                ('song', models.ForeignKey(blank=True, default=None, on_delete=django.db.models.deletion.CASCADE, to='song.song')),
            ],
        ),
    ]
