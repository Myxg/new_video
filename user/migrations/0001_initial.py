# Generated by Django 2.0.6 on 2020-04-16 01:16

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='UserInfo',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('username', models.CharField(max_length=16)),
                ('password', models.CharField(max_length=20)),
                ('pow', models.CharField(max_length=20)),
            ],
            options={
                'db_table': 'userinfo',
            },
        ),
    ]
