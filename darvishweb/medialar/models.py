from django.db import models


class Table9(models.Model):
    sequence = models.IntegerField(verbose_name="Tartib raqami")
    file_id = models.CharField(verbose_name="Fayl ID", max_length=200, null=True, blank=True)
    file_type = models.CharField(verbose_name="Fayl turi", max_length=20, null=True, blank=True)
    category = models.CharField(verbose_name="Kategoriya", max_length=150, null=True)
    subcategory = models.CharField(verbose_name="Subkategoriya", max_length=150, null=True)
    caption = models.TextField(verbose_name="Tavsif", null=True)
    link = models.CharField(verbose_name="Youtube link", max_length=200, null=True, blank=True)

    class Meta:
        verbose_name = 'Suhbat va loyihalar'
        verbose_name_plural = 'Suhbat va loyihalar'


class Table10(models.Model):
    id = models.AutoField(verbose_name="Tartib raqami", primary_key=True)
    file_name = models.CharField(verbose_name="Maqola nomi", max_length=150, null=True)
    link = models.CharField(verbose_name="Maqola linki", max_length=150, null=True)

    class Meta:
        verbose_name = 'Maqolalar'
        verbose_name_plural = 'Maqolalar'


class Tables(models.Model):
    table_number = models.IntegerField(verbose_name='Tartib raqami:', primary_key=True, null=False)
    table_name = models.CharField(verbose_name='Nomi:', max_length=200, null=True)
    table_type = models.CharField(verbose_name='Turi:', max_length=100, null=True)
    channel_id = models.CharField(verbose_name='Kanal ID raqami:', max_length=150, null=True)
    comment = models.TextField(verbose_name='Izohlar:', null=True)
    files = models.BooleanField(verbose_name='Fayllar yuklangan bo\'lsa katakchani belgilab qo\'ying',
                                default=False)

    class Meta:
        verbose_name = 'Dars va kurslar jadvali'
        verbose_name_plural = 'Dars va kurslar jadvali'
