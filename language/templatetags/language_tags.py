from django import template
from language.models import *

register = template.Library()

@register.inclusion_tag('include/list_categories.html')
def get_categories(cat_selected=0):
    cats = Category.objects.all()
    return {'cats': cats, 'cat_selected': cat_selected}