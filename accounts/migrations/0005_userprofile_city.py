# Generated by Django 5.2 on 2025-04-30 18:49

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0004_alter_user_role'),
    ]

    operations = [
        migrations.AddField(
            model_name='userprofile',
            name='city',
            field=models.CharField(blank=True, max_length=15, null=True),
        ),
    ]
