# Generated by Django 4.2.3 on 2023-07-09 18:10

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0002_article_englishtitle'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='article',
            name='englishTitle',
        ),
    ]
