# models.py
from django.db import models
from django.contrib.auth import get_user_model
from django.contrib.auth.models import User



User = get_user_model()

class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    age = models.IntegerField()
    school = models.CharField(max_length=255)

    def __str__(self):
        return self.user.username
    
    
class Category(models.Model):
    name = models.CharField(max_length=200)

    def __str__(self):
        return self.name



class Book(models.Model):
    category = models.ForeignKey(Category, on_delete=models.CASCADE, related_name='books', null=True,blank=True)
    title = models.CharField(max_length=255)
    author = models.CharField(max_length=255)
    image = models.ImageField(upload_to='books/images/')
    pdf = models.FileField(upload_to='books/pdfs/')
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.title
    

class SelectedBook(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    book = models.ForeignKey(Book, on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        unique_together = ('user', 'book') 

    def __str__(self):
        return f"{self.user} - {self.book}"    