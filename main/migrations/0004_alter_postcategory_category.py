# Generated by Django 4.1.1 on 2022-11-15 18:15

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0003_remove_postcategory_user_postcategory_category'),
    ]

    operations = [
        migrations.AlterField(
            model_name='postcategory',
            name='category',
            field=models.ForeignKey(default='Category.objects.get(pk=1)', on_delete=django.db.models.deletion.CASCADE, to='main.category'),
        ),
    ]
