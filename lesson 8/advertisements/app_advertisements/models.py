from django.db import models
from django.contrib import admin
# Create your models here.
class Advertisement(models.Model):
    title = models.CharField('Заголовок', max_length=128)
    description = models.TextField('Описание')
    price = models.DecimalField('Цена', max_digits=10, decimal_places=2)
    auction = models.BooleanField('Торг', help_text='Отметьте, если торг нужен')
    create_at = models.DateTimeField(auto_now_add=True)
    update_at = models.DateTimeField(auto_now=True)

    @admin.display(description='Дата создания')
    def create_date(self):
        from django.utils import timezone, html
        if self.create_at.date() == timezone.now().date():
            create_time = self.create_at.time().strftime('%H:%M')
            return html.format_html(
                '<span style = "color:green; font-weight: bold;">Сегодня в {}</span>', create_time
            )
        return self.create_at.strftime('%d.%m.%Y в %H:%M')

    @admin.display(description='Дата обновления')
    def update_date(self):
        from django.utils import timezone, html
        if self.update_at.date() == timezone.now().date():
            update_time = self.update_at.time().strftime('%H:%M')
            return html.format_html(
                '<span style = "color:red; font-weight: bold;">Сегодня в {}</span>', update_time
            )
        return self.update_at.strftime('%d.%m.%Y в %H:%M')


    def __str__(self):
        return f'Advertisement(id={self.id}, title={self.title}, price={self.price})'

    class Meta:
        db_table = 'advertisements'
        app_label = 'app_advertisements'

