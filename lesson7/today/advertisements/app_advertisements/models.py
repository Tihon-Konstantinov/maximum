from django.db import models
from django.db import connections

class Advertisements(models.Model):
    title = models.CharField('Заголовок', max_length=128)
    price = models.DecimalField('Цена', max_digits=10, decimal_places=2)
    discription = models.TextField('Описание')
    person_http = models.TextField('Ссылка на человека')
    auction = models.BooleanField('Торг', help_text='Отметьте, если торг нужен')
    create_date = models.DateTimeField(auto_now_add=True)
    update_date = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f"Advertisements(id={self.id}, title={self.title}, price={self.price}"

    class Meta:
        db_table = 'advertisements'
