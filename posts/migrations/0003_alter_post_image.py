# Generated by Django 3.2.16 on 2023-03-23 10:38

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('posts', '0002_post_image_filter'),
    ]

    operations = [
        migrations.AlterField(
            model_name='post',
            name='image',
            field=models.ImageField(blank=True, default='../default-img_e2wxci', upload_to='images/'),
        ),
    ]
