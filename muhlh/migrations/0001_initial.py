# Generated by Django 2.2.12 on 2022-01-02 01:50

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Post',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('post_slug', models.SlugField(max_length=255, unique=True)),
                ('post_title', models.CharField(db_index=True, max_length=255)),
                ('post_description', models.TextField()),
                ('post_body', models.TextField()),
                ('post_created', models.DateTimeField(auto_now_add=True)),
                ('post_updated', models.DateTimeField(auto_now=True)),
            ],
        ),
    ]
