# Generated by Django 4.0.2 on 2022-02-16 10:09

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('instagram', '0003_post_author'),
    ]

    operations = [
        migrations.AlterField(
            model_name='post',
            name='is_public',
            field=models.BooleanField(db_index=True, default=False),
        ),
    ]
