# Generated by Django 4.2.6 on 2023-10-07 18:28

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='club',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('email', models.EmailField(max_length=254)),
                ('password', models.CharField(max_length=20)),
            ],
        ),
        migrations.CreateModel(
            name='clubevents',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('cname', models.CharField(max_length=30)),
                ('cemail', models.CharField(max_length=30)),
                ('ename', models.CharField(max_length=100)),
                ('edate', models.CharField(max_length=30)),
                ('evenue', models.CharField(max_length=100)),
                ('etime', models.CharField(max_length=20)),
                ('etype', models.CharField(max_length=20)),
                ('edesc', models.CharField(max_length=400)),
                ('eligibility', models.CharField(max_length=30)),
                ('elink', models.CharField(max_length=400)),
                ('efee', models.CharField(max_length=400)),
            ],
        ),
    ]
