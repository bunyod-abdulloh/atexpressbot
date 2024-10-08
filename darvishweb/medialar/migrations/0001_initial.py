# Generated by Django 5.1 on 2024-08-14 06:28

from django.db import migrations, models


class Migration(migrations.Migration):
    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Table10',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False, verbose_name='Tartib raqami')),
                ('file_name', models.CharField(max_length=150, null=True, verbose_name='Maqola nomi')),
                ('link', models.CharField(max_length=150, null=True, verbose_name='Maqola linki')),
            ],
            options={
                'verbose_name': 'Maqolalar',
                'verbose_name_plural': 'Maqolalar',
            },
        ),
        migrations.CreateModel(
            name='Table9',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('sequence', models.IntegerField(verbose_name='Tartib raqami')),
                ('file_id', models.CharField(blank=True, max_length=200, null=True, verbose_name='Fayl ID')),
                ('file_type', models.CharField(blank=True, max_length=20, null=True, verbose_name='Fayl turi')),
                ('category', models.CharField(max_length=150, null=True, verbose_name='Kategoriya')),
                ('subcategory', models.CharField(max_length=150, null=True, verbose_name='Subkategoriya')),
                ('caption', models.TextField(null=True, verbose_name='Tavsif')),
                ('link', models.CharField(blank=True, max_length=200, null=True, verbose_name='Youtube link')),
            ],
            options={
                'verbose_name': 'Suhbat va loyihalar',
                'verbose_name_plural': 'Suhbat va loyihalar',
            },
        ),
        migrations.CreateModel(
            name='Tables',
            fields=[
                ('table_number', models.IntegerField(primary_key=True, serialize=False, verbose_name='Tartib raqami:')),
                ('table_name', models.CharField(max_length=200, null=True, verbose_name='Nomi:')),
                ('table_type', models.CharField(max_length=100, null=True, verbose_name='Turi:')),
                ('channel_id', models.CharField(max_length=150, null=True, verbose_name='Kanal ID raqami:')),
                ('comment', models.TextField(null=True, verbose_name='Izohlar:')),
                ('files', models.BooleanField(default=False,
                                              verbose_name="Fayllar yuklangan bo'lsa katakchani belgilab qo'ying")),
            ],
            options={
                'verbose_name': 'Dars va kurslar jadvali',
                'verbose_name_plural': 'Dars va kurslar jadvali',
            },
        ),
    ]
