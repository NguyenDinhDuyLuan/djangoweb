# Generated by Django 4.2 on 2023-05-03 08:56

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('projects', '0006_alter_project_feature_image'),
    ]

    operations = [
        migrations.AlterField(
            model_name='project',
            name='feature_image',
            field=models.ImageField(blank=True, null=True, upload_to=''),
        ),
    ]
