# Generated by Django 4.2.2 on 2023-07-02 13:05

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('myapp', '0003_user_organization_alter_article_title_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='article',
            name='recommended_literature',
            field=models.TextField(default=''),
        ),
    ]