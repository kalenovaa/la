# Generated by Django 4.2.16 on 2024-10-21 13:52

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('posts', '0003_rename_descriptions_login_description_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='login',
            name='position',
            field=models.PositiveIntegerField(default=1),
            preserve_default=False,
        ),
    ]