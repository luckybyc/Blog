from django.db import models
from django.contrib.auth.models import User
class Entry(models.Model):
    Entry_title=models.CharField(max_length=50)
    Entry_text=models.TextField()
    Entry_image=models.ImageField(upload_to='images/')
    Entry_date=models.DateTimeField(auto_now_add=True)
    Entry_author=models.ForeignKey(User,on_delete=models.CASCADE)
    class Meta:
        verbose_name_plural='Entries'
    def __str__(self):
        return f'{self.Entry_title}'