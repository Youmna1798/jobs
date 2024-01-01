from django.db import models
from django.utils import timezone
from django.core.exceptions import ValidationError
from django.core.validators import URLValidator, EmailValidator
from django.core.validators import RegexValidator
from ckeditor.fields import RichTextField

# Create your models here.
# models.py

from django.db import models

class Job(models.Model):
    title = models.CharField(max_length=255, verbose_name="العنوان")
    description = RichTextField(verbose_name="الوصف")
    # application_link = models.URLField()
    image = models.ImageField(upload_to='static/job_images/', null=True, blank=True, verbose_name="رفع الصورة")

    published_date = models.DateTimeField(default=timezone.now)
    apply = models.CharField(
        max_length=255,
        default='',
        validators=[
            RegexValidator(
                regex=r'^(https?://\S+|\S+@\S+)$',
                message='Enter a valid URL or email.',
            ),
        ],
        verbose_name="لينك او ايميل التقديم"
    )
    def get_apply_link(self):
        # Check if the apply field is an email
        if '@' in self.apply:
            return f'mailto:{self.apply}'  # Use mailto: scheme for emails
        return self.apply  # Assume it's a URL if not an email
    def __str__(self):
        return self.title
    

# class Page(models.Model):

#     title = models.CharField(max_length=200)

#     description = RichTextField()
#     def __str__(self):
#         return self.title
    
# class NewPage(models.Model):
#     title = models.CharField(max_length=255)
#     description = RichTextField()
#     published_date = models.DateTimeField(default=timezone.now)
#     apply = models.CharField(
#         max_length=255,
#         default='',
#     )
#     def get_apply_link(self):
#         # Check if the apply field is an email
#         if '@' in self.apply:
#             return f'mailto:{self.apply}'  # Use mailto: scheme for emails
#         return self.apply  # Assume it's a URL if not an email
#     def __str__(self):
#         return self.title