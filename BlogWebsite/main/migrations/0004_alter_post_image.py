# Generated by Django 5.0.3 on 2024-03-18 08:56

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0003_remove_post_category_choices_post_category'),
    ]

    operations = [
        migrations.AlterField(
            model_name='post',
            name='image',
            field=models.ImageField(default='images/default_img.jpg', upload_to='images/'),
        ),
    ]
