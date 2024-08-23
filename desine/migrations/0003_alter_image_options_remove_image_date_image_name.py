# Generated by Django 4.2.3 on 2023-09-08 12:46

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('desine', '0002_alter_image_date'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='image',
            options={'verbose_name': 'عکس ها'},
        ),
        migrations.RemoveField(
            model_name='image',
            name='date',
        ),
        migrations.AddField(
            model_name='image',
            name='name',
            field=models.CharField(default=1, max_length=100),
            preserve_default=False,
        ),
    ]
