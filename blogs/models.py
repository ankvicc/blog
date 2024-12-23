from django.db import models

class BlogPost(models.Model):
    title = models.CharField(max_length=200)  # Заголовок
    text = models.TextField()                 # Текст
    date_added = models.DateTimeField(auto_now_add=True)  # Дата создания

    def __str__(self):
        return self.title
