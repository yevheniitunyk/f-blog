from django.contrib import admin
from .models import PostsModel, CategoryModel, Comments
# Register your models here.


admin.site.register(PostsModel)
admin.site.register(CategoryModel)
admin.site.register(Comments)
