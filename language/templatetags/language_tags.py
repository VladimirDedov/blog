import random

from django import template
from language.models import *

register = template.Library()


@register.inclusion_tag('include/list_categories.html')
def get_categories(cat_selected=0):
    cats = Category.objects.all()
    return {'cats': cats, 'cat_selected': cat_selected}


@register.simple_tag()
def get_testimonial():
    """return list of querysets for footer template"""
    max_id = Testimonial.objects.all().count()
    testimonial = []
    id_list = []
    while True:
        id = random.randint(1, max_id)
        if id not in id_list:
            id_list.append(id)
            testimonial.append(Testimonial.objects.get(id=id))

        if len(testimonial) == 2:
            if len(id_list) >=6:
                id_list=None
            funny=testimonial[:]
            testimonial=None
            return funny
