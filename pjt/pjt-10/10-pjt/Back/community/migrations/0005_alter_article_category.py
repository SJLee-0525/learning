# Generated by Django 4.2.16 on 2024-11-25 04:45

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('community', '0004_comment'),
    ]

    operations = [
        migrations.AlterField(
            model_name='article',
            name='category',
            field=models.CharField(choices=[('FREE', '자유'), ('ASK', '질문'), ('REVIEW', '후기'), ('ETC', '기타'), ('NOTIFICATION', '공지')], default='FREE', max_length=15, verbose_name='질문카테고리'),
        ),
    ]