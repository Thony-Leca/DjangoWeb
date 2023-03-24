from django.db import models
from phonenumber_field.modelfields import PhoneNumberField


class Category(models.Model):
    name = models.CharField(max_length=255)

    class Meta:
        verbose_name_plural = 'Categories'

    def __str__(self):
        return self.name


class Servicios(models.Model):
    name = models.CharField(max_length=255)
    description = models.TextField()
    price = models.IntegerField()
    category = models.ForeignKey(Category, on_delete=models.CASCADE, related_name='servicio')
    is_active = models.BooleanField(default=True)

    class Meta:
        verbose_name_plural = 'Servicios'

    def __str__(self):
        return self.name
    
    @property
    def category_name(self):
        return self.category.name

class Cliente(models.Model):
    name = models.CharField(max_length=255)
    last_name = models.CharField(max_length=255)
    email = models.EmailField(max_length=255)
    telephone = models.CharField(max_length=20)
    description = models.TextField()
    atendido = models.BooleanField(default=False)

    class Meta:
        verbose_name_plural = "Clientes"
    
    def __str__(self):
        return self.name