from django.shortcuts import get_object_or_404, render_to_response
from zeloplus.models import Category


def category_detail(request, slug):
    category = get_object_or_404(Category, slug=slug)
    return render_to_response('zeloplus/category_detail.html',
                              {'object_list': Category.live_entry_set(category),
                               'category': category})


