# Generated by Django 4.0.4 on 2022-04-30 08:27

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Register',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=30)),
                ('phone', models.CharField(max_length=20)),
                ('email', models.EmailField(max_length=254)),
                ('group', models.CharField(max_length=20)),
                ('college', models.CharField(max_length=30)),
            ],
        ),
    ]