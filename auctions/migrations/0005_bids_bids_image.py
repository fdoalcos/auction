# Generated by Django 4.0.5 on 2022-07-17 19:45

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('auctions', '0004_alter_listing_category'),
    ]

    operations = [
        migrations.AddField(
            model_name='bids',
            name='bids_image',
            field=models.ImageField(blank=True, null=True, upload_to='category/'),
        ),
    ]