# Generated by Django 3.0.8 on 2020-07-04 17:54

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='messages',
            old_name='msg_body',
            new_name='s_msg_body',
        ),
        migrations.AddField(
            model_name='messages',
            name='r_msg_body',
            field=models.CharField(default='', max_length=500),
        ),
    ]
