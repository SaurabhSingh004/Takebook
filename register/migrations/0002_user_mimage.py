# Generated by Django 3.0.3 on 2020-09-05 09:59

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('register', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='user',
            name='mImage',
            field=models.TextField(default='static/register/images/user.png'),
        ),
    ]
