# Generated by Django 3.0 on 2021-05-10 09:44

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='vaccinated',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=128)),
                ('adhar', models.IntegerField(max_length=15)),
                ('mobile', models.IntegerField(max_length=11)),
                ('dob', models.CharField(max_length=30)),
                ('pic', models.ImageField(upload_to='images/')),
            ],
        ),
    ]
