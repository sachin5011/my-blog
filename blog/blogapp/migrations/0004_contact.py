# Generated by Django 4.0.2 on 2023-01-30 07:46

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blogapp', '0003_alter_about_abt_title'),
    ]

    operations = [
        migrations.CreateModel(
            name='Contact',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=200)),
                ('email', models.EmailField(max_length=150)),
                ('phone', models.CharField(max_length=14)),
                ('message', models.TextField()),
            ],
        ),
    ]
