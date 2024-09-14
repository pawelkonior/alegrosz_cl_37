from django.db import models
from django.utils.text import slugify


class Modified(models.Model):
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        abstract = True


class Product(Modified):
    name = models.CharField(max_length=100)  # <input type='text'>
    description = models.TextField(default="", blank=True)  # <textarea></textarea>
    price = models.DecimalField(max_digits=6, decimal_places=2)  # <input type='number'>
    stock_count = models.IntegerField(help_text="How manu items are currently in stock")
    sku = models.CharField(max_length=20, verbose_name="Stock Keeping Unit")
    slug = models.SlugField(blank=True, unique=True)

    def __str__(self):
        return self.name

    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = slugify(self.name)
        return super().save(*args, **kwargs)


class ProductImage(models.Model):
    image = models.ImageField(upload_to='product_images')  # Pil (Pillow)
    product = models.ForeignKey('Product', on_delete=models.CASCADE, related_name='images')

    def __str__(self):
        return str(self.image)


class Category(models.Model):
    name = models.CharField(max_length=20)
    products = models.ManyToManyField('Product', related_name='categories')

    def __str__(self):
        return self.name

    class Meta:
        verbose_name_plural = 'Categories'
        verbose_name = 'Product Category'
        ordering = ('name',)
