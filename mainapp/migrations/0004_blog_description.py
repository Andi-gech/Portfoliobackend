# Generated by Django 4.2.2 on 2023-09-25 20:49

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('mainapp', '0003_alter_blog_content'),
    ]

    operations = [
        migrations.AddField(
            model_name='blog',
            name='description',
            field=models.TextField(default='jjj'),
            preserve_default=False,
        ),
    ]
