# Generated by Django 4.2.7 on 2023-11-17 01:21

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('News', '0003_berita_deskripsi_berita_kategoriid_berita_publikasi_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='berita',
            name='kategoriID',
            field=models.IntegerField(default=255),
            preserve_default=False,
        ),
    ]