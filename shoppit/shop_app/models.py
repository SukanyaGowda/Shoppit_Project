from django.db import models
from django.utils.text import slugify

# Create your models here.
class Product(models.Model):
    CATEGORY=(("Electronics","ELECTRONICS"),
             ("Groceries","GROCERIES"),
             ("Clothings","CLOTHINGS")
    )
    name=models.CharField(max_length=100 )
    slung=models.SlugField(blank=True , null=True)
    image=models.ImageField( upload_to="image")
    descriptions=models.TextField(blank=True , null=True)
    price=models.DecimalField(max_digits=10 , decimal_places=2)
    category=models.CharField(max_length=15,choices=CATEGORY , blank=True , null=True)
    

    def __str__(self):
        return self.name
    

    def save(self, *args, **kwargs):
        if not self.slung:
            self.slung=slugify(self.name)
            unique_slug=self.slung
            counter=1
            if Product.objects.filter(slung=unique_slug).exists():
               unique_slug=f'{self.slung}-{counter}'
               counter+=1
            self.slung=unique_slug
    

        super().save(*args, **kwargs)


    
    