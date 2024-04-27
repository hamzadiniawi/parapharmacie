# Generated by Django 5.0.4 on 2024-04-27 17:33

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('myapp', '0003_remove_admin_password_remove_client_password_and_more'),
    ]

    operations = [
        migrations.RenameField(
            model_name='admin',
            old_name='role',
            new_name='department',
        ),
        migrations.RemoveField(
            model_name='client',
            name='role',
        ),
        migrations.RemoveField(
            model_name='manager',
            name='role',
        ),
        migrations.AddField(
            model_name='user',
            name='role',
            field=models.CharField(default=1, max_length=255),
            preserve_default=False,
        ),
    ]
