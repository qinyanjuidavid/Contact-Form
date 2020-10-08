from django.db import models
from ckeditor.fields import RichTextField



class Feedback(models.Model):
    name=models.CharField(max_length=200,help_text="Name of the sender")
    email=models.EmailField(max_length=200)
    subject=models.CharField(max_length=200)
    message=RichTextField()
    date=models.DateTimeField(auto_now_add=True)

    class Meta:
        verbose_name_plural="Feedback"
    def __str__(self):
        return f"{self.name} - {self.email}"
