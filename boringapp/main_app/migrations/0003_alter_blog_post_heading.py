# Generated by Django 3.2.4 on 2021-08-05 07:02

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main_app', '0002_alter_blog_post_paragraph'),
    ]

    operations = [
        migrations.AlterField(
            model_name='blog_post',
            name='heading',
            field=models.CharField(max_length=100),
        ),
    ]
