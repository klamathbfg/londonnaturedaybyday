# Generated by Django 5.1.4 on 2024-12-16 01:59

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('articles', '0003_article_blog_image'),
    ]

    operations = [
        migrations.AddField(
            model_name='article',
            name='youtube_video',
            field=models.CharField(blank=True, max_length=200, null=True),
        ),
    ]
