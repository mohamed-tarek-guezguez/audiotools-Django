from django.shortcuts import render, redirect
from .models import Product, Contact
from django.core.paginator import Paginator

from django.http import HttpResponse
from django.shortcuts import get_object_or_404
from django.conf import settings
import os

from django.db.models import Q
from .filters import CategoryFilter
from .forms import contactForm

import re
def mobile(request):
    MOBILE_AGENT_RE=re.compile(r".*(iphone|mobile|androidtouch)",re.IGNORECASE)

    if MOBILE_AGENT_RE.match(request.META['HTTP_USER_AGENT']):
        return True
    else:
        return False

# Create your views here.
def homePage(request):

    prods = Product.objects.all().order_by('-id')
    
    q = request.GET.get('q')
    if q:
        words = request.GET.get('q').split(" ")
        q_filters = Q()
        for word in words:
            q_filters |= Q(Title__icontains=word)
        prods = Product.objects.filter(q_filters)
    
    query = request.GET.get('Category__contains')
    myCatFilter = CategoryFilter(request.GET, queryset=prods)
    prods = myCatFilter.qs

    paginator = Paginator(prods, 18)
    try:
        page = int(request.GET.get('page', '1'))
    except:
        page = 1
    try:
        prods = paginator.page(page)
    except(EmptyPage, InvalidPage):
        prods = paginator.page(paginator.num_pages)

    if request.method == 'POST':
        form = contactForm(request.POST, request.FILES)

        if form.is_valid():
            form.save()

        return redirect('/')
    else:
        form = contactForm()

    if mobile(request):
        is_mobile = 1
    else:
        is_mobile = 2
    
    is_mobile_negative = is_mobile * -1

    context = {
        'prods': prods,
        'myCatFilter': myCatFilter,
        'form': form,
        'query': query,
        'tquery': q,
        'is_mobile': is_mobile,
        'is_mobile_negative': is_mobile_negative,
    }

    return render(request, 'index.html', context)

def prodDetail(request, slug):
    prod = Product.objects.get(Slug=slug)
    return render(request, 'prodDetail.html', {'prod': prod})