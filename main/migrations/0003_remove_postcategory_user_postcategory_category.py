# Generated by Django 4.1.1 on 2022-11-15 18:13

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0002_rename_auther_post_author'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='postcategory',
            name='user',
        ),
        migrations.AddField(
            model_name='postcategory',
            name='category',
            field=models.ForeignKey(default='Null', on_delete=django.db.models.deletion.CASCADE, to='main.category'),
        ),
    ]