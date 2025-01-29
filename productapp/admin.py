from django.contrib import admin # type: ignore

from productapp.models import Product # type: ignore

# Register your models here.

admin.site.register(Product)