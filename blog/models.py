from django.db import models
from django.utils import timezone

class Post(models.Model):
    CATEGORY_CHOICES = (
        ('Technology', 'Technology'),
        ('Travel', 'Travel'),
        ('Sports', 'Sports'),
        ('News', 'News'),
        ('Music', 'Music'),
        ('Work', 'Work'),
    )
    title = models.CharField(max_length=1000, default='')
    slug = models.SlugField()
    text = models.TextField() 
    text_2 = models.TextField(default='')
    created_date = models.DateTimeField(default='')
    category = models.CharField(max_length=200, default='', choices=CATEGORY_CHOICES)
    cover = models.FileField(default='')
    author = models.CharField(max_length=50000, default='')
    cover2 = models.FileField(default='')
    large_heading = models.CharField(max_length=500,default='' )
    large_heading_text = models.CharField(max_length=50000, default='')
    quote = models.CharField(max_length=500, default='')
    quotes_name =  models.CharField(max_length=500 ,default='' )
    smaller_heading =  models.CharField(max_length=5000,default='' )
    smaller_heading_text =  models.CharField(max_length=5000,default='' )
    tag1 =  models.CharField(max_length=500, default='')
    tag2 =  models.CharField(max_length=500, default='')
    tag3 =  models.CharField(max_length=500,default='' )

    


    class Meta:
        ordering = ['-created_date']

    def publish(self): 
        self.published_date = timezone.now() 
        self.save() 

    def __str__(self): 
        return self.title 

    

class About(models.Model):
    cover = models.FileField(default='')
    title = models.CharField(max_length=2000)
    about_me = models.CharField(max_length=1000) 
    my_story = models.CharField(max_length=1000)
    about_my_story =  models.CharField(max_length=1000)
    who_we =  models.CharField(max_length=1000)
    about_who_we =  models.CharField(max_length=1000)
    our_mission =  models.CharField(max_length=1000)
    about_our =  models.CharField(max_length=1000)

    def __str__(self):
        return self.title

class Contact(models.Model):
    cover = models.ImageField(upload_to='images/', default='')
    title = models.CharField(max_length=2000)
    about_me = models.CharField(max_length=1000) 
    where_to_find = models.CharField(max_length=1000)
    find_1 =  models.CharField(max_length=1000)
    find_2 =  models.CharField(max_length=1000)
    find_3 =  models.CharField(max_length=1000)
    contact_info =  models.CharField(max_length=1000)
    gmail =  models.CharField(max_length=1000)
    insta =  models.CharField(max_length=1000)
    youtube =  models.CharField(max_length=1000)
    phone =  models.CharField(max_length=1000)
    

    def __str__(self):
        return self.title
