from django.db import models

# Create your models here.
# from django.db import models

# from django.db import models

class Property(models.Model):
    CATEGORY_CHOICES = [
        ('Available', 'Available'),
        ('For Sale', 'For Sale'),  # Fixed typo: 'For Slae' -> 'For Sale'
    ]
    CATEGORY_TYPE_CHOICES = [
        ('Apartment', 'Apartment'),
        ('Property', 'Property'),  # Capitalize to match naming convention
    ]

    title = models.CharField(max_length=200)
    location = models.CharField(max_length=200)
    price = models.DecimalField(max_digits=12, decimal_places=2)
    category = models.CharField(max_length=20, choices=CATEGORY_CHOICES)
    category_type = models.CharField(max_length=20, choices=CATEGORY_TYPE_CHOICES)
    images = models.ImageField(upload_to='property_images/')
    bathroom = models.PositiveIntegerField(blank =True,null= True,default=0)
    bedroom = models.PositiveIntegerField(blank =True,null= True,default=0)

    is_active = models.BooleanField(default=True)

    def __str__(self):
        return self.title
    

 
class Rent(models.Model):
    CATEGORY_CHOICES = [
        ('Available', 'Available'),
        ('For Sale', 'For Sale'),  # Fixed typo: 'For Slae' -> 'For Sale'
    ]
    CATEGORY_TYPE_CHOICES = [
        ('Apartment', 'Apartment'),
        ('Property', 'Property'),  # Capitalize to match naming convention
    ]

    title = models.CharField(max_length=200)
    location = models.CharField(max_length=200)
    price = models.DecimalField(max_digits=12, decimal_places=2)
    category = models.CharField(max_length=20, choices=CATEGORY_CHOICES)
    category_type = models.CharField(max_length=20, choices=CATEGORY_TYPE_CHOICES)
    images = models.ImageField(upload_to='property_images/')
    bathroom = models.PositiveIntegerField(blank =True,null= True,default=0)
    bedroom = models.PositiveIntegerField(blank =True,null= True,default=0)

    is_active = models.BooleanField(default=True)

    def __str__(self):
        return self.title
     
 

class Buy(models.Model):
    CATEGORY_CHOICES = [
        ('Available', 'Available'),
        ('For Sale', 'For Sale'),  # Fixed typo: 'For Slae' -> 'For Sale'
    ]
    CATEGORY_TYPE_CHOICES = [
        ('Apartment', 'Apartment'),
        ('Property', 'Property'),  # Capitalize to match naming convention
    ]

    title = models.CharField(max_length=200)
    location = models.CharField(max_length=200)
    price = models.DecimalField(max_digits=12, decimal_places=2)
    category = models.CharField(max_length=20, choices=CATEGORY_CHOICES)
    category_type = models.CharField(max_length=20, choices=CATEGORY_TYPE_CHOICES)
    images = models.ImageField(upload_to='property_images/')
    bathroom = models.PositiveIntegerField(blank =True,null= True,default=0)
    bedroom = models.PositiveIntegerField(blank =True,null= True,default=0)

    is_active = models.BooleanField(default=True)

    def __str__(self):
        return self.title
    
    
    
 
class shortlet(models.Model):
    CATEGORY_CHOICES = [
        ('Available', 'Available'),
        ('For Sale', 'For Sale'),  # Fixed typo: 'For Slae' -> 'For Sale'
    ]
    CATEGORY_TYPE_CHOICES = [
        ('Apartment', 'Apartment'),
        ('Property', 'Property'),  # Capitalize to match naming convention
    ]

    title = models.CharField(max_length=200)
    location = models.CharField(max_length=200)
    price = models.DecimalField(max_digits=12, decimal_places=2)
    category = models.CharField(max_length=20, choices=CATEGORY_CHOICES)
    category_type = models.CharField(max_length=20, choices=CATEGORY_TYPE_CHOICES)
    images = models.ImageField(upload_to='property_images/')
    bathroom = models.PositiveIntegerField(blank =True,null= True,default=0)
    bedroom = models.PositiveIntegerField(blank =True,null= True,default=0)

    is_active = models.BooleanField(default=True)

    def __str__(self):
        return self.title
    

class Land(models.Model):
    CATEGORY_CHOICES = [
        ('Available', 'Available'),
        ('For Sale', 'For Sale'),  # Fixed typo: 'For Slae' -> 'For Sale'
    ]
    CATEGORY_TYPE_CHOICES = [
        ('Apartment', 'Apartment'),
        ('land', 'land'),  # Capitalize to match naming convention
    ]

    title = models.CharField(max_length=200)
    location = models.CharField(max_length=200)
    price = models.DecimalField(max_digits=12, decimal_places=2)
    category = models.CharField(max_length=20, choices=CATEGORY_CHOICES)
    category_type = models.CharField(max_length=20, choices=CATEGORY_TYPE_CHOICES)
    images = models.ImageField(upload_to='property_images/')
   
    is_active = models.BooleanField(default=True)

    def __str__(self):
        return self.title
 



class ContactMessage(models.Model):
    name = models.CharField(max_length=100)
    email = models.EmailField()
    message = models.TextField()
    sent_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.name
