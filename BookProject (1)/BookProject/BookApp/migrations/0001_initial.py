# Generated by Django 5.0.3 on 2024-05-19 19:42

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Publisher',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('country', models.CharField(max_length=100)),
                ('city', models.CharField(max_length=100)),
                ('year_of_establishment', models.DateField()),
            ],
        ),
        migrations.CreateModel(
            name='Book',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('image', models.ImageField(upload_to='')),
                ('title', models.CharField(max_length=100)),
                ('page_number', models.IntegerField()),
                ('isbn', models.CharField(max_length=100)),
                ('dimensions', models.CharField(max_length=100)),
                ('year_of_publication', models.IntegerField()),
                ('cover', models.CharField(choices=[('hardCover', 'h'), ('s', 'softCover')], max_length=9)),
                ('price', models.IntegerField()),
                ('category', models.CharField(choices=[('r', 'Romance'), ('t', 'Thriller'), ('Classic', 'k'), ('d', 'Drama'), ('History', 'h')], max_length=7)),
                ('publisher', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='BookApp.publisher')),
            ],
        ),
    ]
