from django.db import models

#базовая модель
class BaseModel(models.Model):
    title = models.CharField(max_length=100, blank=False, verbose_name='Название')

    def __str__(self):
        return self.title

    class Meta:
        # так как от данной модели будут наследоваться другие и она не нужна в БД, делаем ее абстрактной
        abstract = True


class Edu_module(BaseModel):
    description = models.CharField(max_length=255, blank=True, verbose_name='Описание')


# разделы модуля
class Section(BaseModel):
    module = models.ForeignKey(to=Edu_module, on_delete=models.SET_NULL, null=True, verbose_name='Модуль')

