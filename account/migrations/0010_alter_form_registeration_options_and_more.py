# Generated by Django 4.2.3 on 2023-09-08 12:25

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('account', '0009_alter_reserve_user'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='form_registeration',
            options={'verbose_name': 'فرم ثبت\u200cنام', 'verbose_name_plural': 'فرم\u200cهای ثبت\u200cنام'},
        ),
        migrations.AlterModelOptions(
            name='reserve',
            options={'verbose_name': 'نوبت رزرو', 'verbose_name_plural': 'نوبت های رزرو'},
        ),
    ]
