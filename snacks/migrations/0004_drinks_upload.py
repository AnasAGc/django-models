# Generated by Django 3.2.6 on 2021-08-30 21:51

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('snacks', '0003_alter_drinks_image'),
    ]

    operations = [
        migrations.AddField(
            model_name='drinks',
            name='upload',
            field=models.FileField(null=True, upload_to='uploads/'),
        ),
    ]
