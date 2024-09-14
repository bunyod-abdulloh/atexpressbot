from django.db import models


class BaseLessonModel(models.Model):
    lesson_number = models.IntegerField(verbose_name="Dars tartib raqami", primary_key=True)
    audio_id = models.CharField(verbose_name="Audio ID", max_length=150, null=True, blank=True)
    photo_id = models.CharField(verbose_name="Rasm ID", max_length=150, null=True, blank=True)
    video_id = models.CharField(verbose_name="Video ID", max_length=150, null=True, blank=True)
    document_id = models.CharField(verbose_name="Document ID", max_length=150, null=True, blank=True)
    file_name = models.CharField(verbose_name="Fayl nomi", max_length=150, null=True)
    caption = models.TextField(verbose_name="Tavsif", max_length=4000, null=True)

    class Meta:
        abstract = True


class Table1(BaseLessonModel):
    class Meta:
        verbose_name = 'Psixoterapiya va psixologiya asoslari'
        verbose_name_plural = 'Psixoterapiya va psixologiya asoslari'


class Table2(BaseLessonModel):
    class Meta:
        verbose_name = 'Tabobat va tibbiyotda mijoz va tepmerament ilmi'
        verbose_name_plural = 'Tabobat va tibbiyotda mijoz va tepmerament ilmi'


class Table3(BaseLessonModel):
    class Meta:
        verbose_name = 'Miyaning neyroplastikligi va neyrobika'
        verbose_name_plural = 'Miyaning neyroplastikligi va neyrobika'


class Table4(BaseLessonModel):
    class Meta:
        verbose_name = 'Ta\'lim va ruhiyat'
        verbose_name_plural = 'Ta\'lim va ruhiyat'


class Table5(BaseLessonModel):
    class Meta:
        verbose_name = 'Farzandim va jigarbandim'
        verbose_name_plural = 'Farzandim va jigarbandim'


class Table6(BaseLessonModel):
    class Meta:
        verbose_name = 'Nafs diagnostikasi'
        verbose_name_plural = 'Nafs diagnostikasi'


class Table7(BaseLessonModel):
    class Meta:
        verbose_name = 'Sharq psixologiyasi va psixoterapiya'
        verbose_name_plural = 'Sharq psixologiyasi va psixoterapiya'


class Table8(BaseLessonModel):
    class Meta:
        verbose_name = 'Ruhiy salomatlik'
        verbose_name_plural = 'Ruhiy salomatlik'
