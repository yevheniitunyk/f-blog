from django import template
from django.db.models import Count, F
from django.shortcuts import redirect, render
from posts.models import Reply
from posts.models import PostsModel
from posts.models import CategoryModel, Comments
from posts.forms import CommentForm

register = template.Library()

@register.simple_tag()
def get_categories():
    return CategoryModel.objects.all()

@register.simple_tag()
def get_comment(title):
    return Comments.objects.filter(post__title=title)

@register.simple_tag()
def get_replies(pk):
    return Reply.objects.filter(comment__pk=pk)