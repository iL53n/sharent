# Generated by Django 4.2.1 on 2023-05-15 14:20

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Item',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=200, verbose_name='Title')),
                ('description', models.TextField(verbose_name='Description')),
                ('price', models.CharField(max_length=200, verbose_name='Price')),
                ('location', models.CharField(max_length=200, verbose_name='Location')),
                ('contacts', models.CharField(max_length=200, verbose_name='Contacts')),
                ('cms_img', models.ImageField(upload_to='items_img/')),
            ],
            options={
                'verbose_name': 'Item',
                'verbose_name_plural': 'Items',
            },
        ),
    ]