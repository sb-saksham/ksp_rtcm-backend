# Generated by Django 4.2.11 on 2024-04-10 12:37

from django.db import migrations, models
import django.db.models.deletion
import traffic_image.models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Junction',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('name', models.CharField(blank=True, max_length=264, null=True)),
                ('lat', models.FloatField(blank=True, null=True)),
                ('long', models.FloatField(blank=True, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='TrafficImage',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('direction', models.CharField(blank=True, choices=[('north', 'NORTH'), ('south', 'SOUTH'), ('east', 'EAST'), ('west', 'WEST')], max_length=5, null=True)),
                ('image', models.ImageField(upload_to=traffic_image.models.traffic_directory_path)),
                ('junction', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='traffic_images', to='traffic_image.junction')),
            ],
        ),
    ]