from django.shortcuts import render, get_object_or_404
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from django.http import JsonResponse

from .models import Work


def work_list(request):
    work_list = Work.published.all()
    paginator = Paginator(work_list, per_page = 5)
    page_number = request.GET.get('page', 1)

    try:
        works = paginator.page(page_number)
    except PageNotAnInteger:
        # If page_number is not an integer deliver the first page
        works = paginator.page(1)    
    except EmptyPage:
        # If page_number is out of range deliver last page of results
        works = paginator.page(paginator.num_pages)
    
    contex = {
        'works': works
    }
    return render(request, 'maint/work-list.html', contex)



def work_detail(request, work):
    work = get_object_or_404(Work, slug=work, status=Work.Status.PUBLISHED)
    contex = {
        'work': work
    }
    return render(request, 'maint/work-detail.html', contex)

