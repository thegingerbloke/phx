# Generated by Django 2.1 on 2018-08-21 07:55

import ckeditor.fields
from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('gallery', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Announcement',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('announcement', ckeditor.fields.RichTextField()),
                ('display_until', models.DateTimeField()),
                ('created_date', models.DateTimeField(auto_now_add=True)),
                ('modified_date', models.DateTimeField(auto_now=True)),
                ('author', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='Content',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=32)),
                ('join', ckeditor.fields.RichTextField()),
                ('events', ckeditor.fields.RichTextField()),
                ('about', ckeditor.fields.RichTextField()),
                ('gallery', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='gallery.Gallery')),
            ],
            options={
                'verbose_name': 'home page content',
                'verbose_name_plural': 'home page content',
            },
        ),
        migrations.CreateModel(
            name='Hero',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('image', models.ImageField(help_text='Hero images should be at least 1200 pixels wide, with an aspect ratio of at least 16:9.', upload_to='home/hero/')),
                ('caption', models.CharField(blank=True, max_length=200)),
                ('created_date', models.DateTimeField(auto_now_add=True)),
                ('modified_date', models.DateTimeField(auto_now=True)),
                ('author', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='HeroImageCategory',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('category', models.CharField(max_length=30)),
                ('count', models.PositiveIntegerField()),
            ],
            options={
                'verbose_name_plural': 'hero image categories',
            },
        ),
        migrations.AddField(
            model_name='hero',
            name='image_categories',
            field=models.ManyToManyField(blank=True, to='home.HeroImageCategory'),
        ),
    ]