# Generated by Django 4.2.16 on 2024-11-20 05:42

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('community', '0002_article_like_users_alter_article_user'),
    ]

    operations = [
        migrations.AddField(
            model_name='article',
            name='category',
            field=models.CharField(choices=[('FREE', '자유'), ('ASK', '질문'), ('REVIEW', '후기'), ('ETC', '기타')], default='FREE', max_length=15, verbose_name='질문카테고리'),
        ),
    ]