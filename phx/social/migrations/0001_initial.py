# Generated by Django 2.1 on 2018-08-21 07:55

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Social',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('model', models.CharField(max_length=20)),
                ('title', models.CharField(max_length=200)),
                ('url', models.URLField()),
                ('created_date', models.DateTimeField(auto_now_add=True)),
                ('modified_date', models.DateTimeField(auto_now=True)),
                ('posted', models.BooleanField(default=False)),
                ('reposted', models.BooleanField(default=False)),
            ],
            options={
                'verbose_name': 'social media post',
            },
        ),
    ]