from django.db import models
from django.contrib.auth.models import User
from django.urls import reverse
# Create your models here.


class Base(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)
    class Meta:
        abstract = True
        ordering = ('-created_at',)


class CategoryModel(models.Model):
    title = models.CharField(max_length=150)

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return reverse('show_by_category', args=[self.title])



class PostsModel(Base):
    title = models.CharField(max_length=200)
    content = models.TextField(blank=True)
    # created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    photo = models.ImageField(upload_to='photos/%Y/%m/%d/', blank=True)
    views = models.IntegerField(default=0)
    category = models.ForeignKey(CategoryModel, on_delete=models.CASCADE)
    published = models.BooleanField(default=True)
    # user = models.ForeignKey(User, on_delete=models.CASCADE)

    def __str__(self):
        return self.title


    def get_absolute_url(self):
        return reverse('show_detail', args=[self.title])


    # class Meta:
    #     ordering = ('-created_at',)


class Comments(Base):
    content = models.CharField(max_length=401)
    # created_at = models.DateTimeField(auto_now_add=True)
    # user = models.ForeignKey(User, on_delete=models.CASCADE)
    post = models.ForeignKey(PostsModel, on_delete=models.PROTECT)

    # class Meta:
    #     ordering = ('-created_at',)


class Reply(Base):
    comment = models.ForeignKey(Comments, on_delete=models.CASCADE)
    # user = models.ForeignKey(User, on_delete=models.CASCADE)
    content = models.CharField(max_length=401)
    # created_at = models.DateTimeField(auto_now_add=True)

    # class Meta:
    #     ordering = ('-created_at',)