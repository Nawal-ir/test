# Generated by Django 5.0.3 on 2024-03-17 17:20

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Post',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=200)),
                ('content', models.TextField()),
                ('is_published', models.BooleanField()),
                ('published_at', models.DateTimeField(auto_now_add=True)),
                ('poster', models.ImageField(default='images/default.jpg', upload_to='images/')),
                ('category_choices', models.CharField(choices=[('General', 'General'), ('Science', 'Science'), ('Culture', 'Culture'), ('Food', 'Food'), ('Tech', 'Tech'), ('Fashion', 'Fashion')], default='General', max_length=10)),
            ],
        ),
    ]