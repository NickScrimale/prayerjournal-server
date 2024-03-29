# Generated by Django 4.1.6 on 2023-05-13 16:47

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='User',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('uid', models.CharField(max_length=50)),
                ('first_name', models.CharField(max_length=25)),
                ('last_name', models.CharField(max_length=25)),
                ('profile_image_url', models.CharField(max_length=200)),
            ],
        ),
        migrations.CreateModel(
            name='Version',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('label', models.CharField(max_length=50)),
            ],
        ),
        migrations.CreateModel(
            name='Verse',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('verse', models.TextField(max_length=100)),
                ('content', models.TextField(max_length=1000)),
                ('uid', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='fullstackcapapi.user')),
                ('version_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='fullstackcapapi.version')),
            ],
        ),
        migrations.CreateModel(
            name='UserLike',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('verse', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='fullstackcapapi.verse')),
            ],
        ),
        migrations.CreateModel(
            name='Prayer',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('content', models.TextField(max_length=800)),
                ('pub_date', models.TextField(max_length=800)),
                ('uid', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='fullstackcapapi.user')),
            ],
        ),
    ]
