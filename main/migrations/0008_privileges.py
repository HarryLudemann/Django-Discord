# Generated by Django 3.2 on 2021-06-01 06:07

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('main', '0007_auto_20210601_1306'),
    ]

    operations = [
        migrations.CreateModel(
            name='Privileges',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('identifier', models.CharField(max_length=50)),
                ('funinspire', models.CharField(max_length=50)),
                ('funcomeback', models.CharField(max_length=50)),
                ('funcat', models.CharField(max_length=50)),
                ('fundog', models.CharField(max_length=50)),
                ('funfox', models.CharField(max_length=50)),
                ('basicping', models.CharField(max_length=50)),
                ('adminquit', models.CharField(max_length=50)),
                ('adminchangeprefix', models.CharField(max_length=50)),
                ('admintest', models.CharField(max_length=50)),
            ],
        ),
    ]