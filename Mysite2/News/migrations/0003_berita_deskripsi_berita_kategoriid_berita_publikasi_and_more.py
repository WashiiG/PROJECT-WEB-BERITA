# Generated by Django 4.2.7 on 2023-11-16 01:05

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('News', '0002_berita_fotopenulis'),
    ]

    operations = [
        migrations.AddField(
            model_name='berita',
            name='deskripsi',
            field=models.CharField(default=255, max_length=255),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='berita',
            name='kategoriID',
            field=models.IntegerField(max_length=255, null=True),
        ),
        migrations.AddField(
            model_name='berita',
            name='publikasi',
            field=models.CharField(default=255, max_length=255),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='berita',
            name='status',
            field=models.CharField(choices=[('publish', 'publish'), ('draft', 'draft')], default=255, max_length=200),
            preserve_default=False,
        ),
    ]
