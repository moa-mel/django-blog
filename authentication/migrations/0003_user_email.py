# Generated by Django 5.0.7 on 2024-07-31 17:21

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('authentication', '0002_alter_user_username'),
    ]

    operations = [
        migrations.AddField(
            model_name='user',
            name='email',
            field=models.EmailField(default='SOME STRING', max_length=255, unique=True),
        ),
    ]
