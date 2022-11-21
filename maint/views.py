from django.shortcuts import render, get_object_or_404

from .models import Work


def work_list(request):
    works = Work.published.all()
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