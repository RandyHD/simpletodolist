# Generated by Django 3.0.2 on 2020-02-06 06:45

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('lists', '0004_item_list'),
    ]

    operations = [
        migrations.AlterField(
            model_name='item',
            name='list',
            field=models.ForeignKey(default=None, on_delete=django.db.models.deletion.CASCADE, to='lists.List'),
        ),
    ]
