from django.db import models


class Bemor(models.Model):
    username = models.CharField(verbose_name="Telegram username", max_length=100, null=True)
    fullname = models.CharField(verbose_name="Familiya Ism Sharif", max_length=255, null=True, blank=True)
    phone = models.CharField(verbose_name="Telefon raqam", max_length=150, null=True, blank=True)
    telegram_id = models.IntegerField(verbose_name="Telegram ID", null=True, blank=True)
    test_type = models.CharField(verbose_name="Test turi", max_length=100, null=True, blank=True)
    file_id = models.CharField(verbose_name="Photo ID", max_length=150, null=True)

    class Meta:
        verbose_name = 'Bemorlar bo\'limi'
        verbose_name_plural = 'Bemorlar bo\'limi'
