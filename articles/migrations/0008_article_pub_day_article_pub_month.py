# Generated by Django 5.1.4 on 2024-12-17 14:59

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('articles', '0007_article_section_link_pub_date_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='article',
            name='pub_day',
            field=models.IntegerField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='article',
            name='pub_month',
            field=models.IntegerField(blank=True, null=True),
        ),
    ]