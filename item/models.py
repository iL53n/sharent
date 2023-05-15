from django.db import models


class Item(models.Model):
    title = models.CharField(max_length=200, verbose_name='Title')
    description = models.TextField(verbose_name='Description')
    price = models.CharField(max_length=200, verbose_name='Price')
    location = models.CharField(max_length=200, verbose_name='Location')
    contacts = models.CharField(max_length=200, verbose_name='Contacts')
    img = models.ImageField(upload_to='items_img/')
    created_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = 'Item'
        verbose_name_plural = 'Items'
