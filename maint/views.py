from django.shortcuts import render, get_object_or_404
from django.core.paginator import Paginator

from .models import Work


def work_list(request):
    work_list = Work.published.all() # lista na site kompletirani opisi na rabota
    # Pagination with 10 work description per page
    # Django uses the Paginator class to split a Queryset object (or other objects with a count() or __len__() method) into Page objects.
    paginator = Paginator(work_list, 10) # broj na opisi na rabota po strana
    #paginator.num_pages # vkupen broj na strani 
    page_number = request.GET.get('page', 1)
    works = paginator.page(page_number)
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