# Generated by Django 5.0.3 on 2024-03-18 15:04

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0004_alter_post_image'),
    ]

    operations = [
        migrations.AlterField(
            model_name='post',
            name='category',
            field=models.CharField(choices=[('General', 'General'), ('Science', 'Science'), ('Culture', 'Culture'), ('Food', 'Food'), ('Tech', 'Tech'), ('Fashion', 'Fashion')], max_length=64),
        ),
    ]