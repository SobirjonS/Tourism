import os

from django.conf import settings
from django.db import models


class New(models.Model):
    title = models.CharField(max_length=255)
    image = models.ImageField(upload_to='news/')
    body = models.TextField()

    def delete(self, *args, **kwargs):
        file_path = os.path.join(settings.MEDIA_ROOT, str(self.image))
        if os.path.isfile(file_path):
            os.remove(file_path)
        super(New, self).delete(*args, **kwargs) # type: ignore
    
    def __str__(self) -> str:
        return self.title
    
    class Meta:
        verbose_name = "Yangilik"
        verbose_name_plural = "Yangiliklar"



class Lendmark(models.Model):
    title = models.CharField(max_length=255)
    image = models.ImageField(upload_to='lendmarks/')
    body = models.TextField()

    def __str__(self) -> str:
        return self.title
    
    class Meta:
        verbose_name = "E`tiborga sazovor joy"
        verbose_name_plural = "E`tiborga sazovor joylar"
    
    def delete(self, *args, **kwargs):
        file_path = os.path.join(settings.MEDIA_ROOT, str(self.image))
        if os.path.isfile(file_path):
            os.remove(file_path)
        super(Lendmark, self).delete(*args, **kwargs) # type: ignore


class Statistic(models.Model):
    title = models.CharField(max_length=255)
    icon = models.ImageField(upload_to='statistic_icons/')
    number = models.IntegerField()

    def __str__(self) -> str:
        return self.title
    
    class Meta:
        verbose_name = "Statistika"
        verbose_name_plural = "Statistikalar"
    
    def delete(self, *args, **kwargs):
        file_path = os.path.join(settings.MEDIA_ROOT, str(self.icon))
        if os.path.isfile(file_path):
            os.remove(file_path)
        super(Statistic, self).delete(*args, **kwargs) # type: ignore


class Hotel(models.Model):
    title = models.CharField(max_length=255)
    image = models.ImageField(upload_to='hotels/')
    body = models.TextField()

    def __str__(self) -> str:
        return self.title
    
    class Meta:
        verbose_name = "Mehmonxona"
        verbose_name_plural = "Mehmonxona"
    
    def delete(self, *args, **kwargs):
        file_path = os.path.join(settings.MEDIA_ROOT, str(self.image))
        if os.path.isfile(file_path):
            os.remove(file_path)
        super(Hotel, self).delete(*args, **kwargs) # type: ignore


class Food(models.Model):
    title = models.CharField(max_length=255)
    image = models.ImageField(upload_to='hotels/')
    body = models.TextField()

    def __str__(self) -> str:
        return self.title
    
    class Meta:
        verbose_name = "Taom"
        verbose_name_plural = "Taomlar"
    
    def delete(self, *args, **kwargs):
        file_path = os.path.join(settings.MEDIA_ROOT, str(self.image))
        if os.path.isfile(file_path):
            os.remove(file_path)
        super(Food, self).delete(*args, **kwargs) # type: ignore

