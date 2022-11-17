from django.shortcuts import render

from .models import Work


def work_list(request):
    works = Work.published.all()
    contex = {
        'works': works
    }
    return render(request, 'maint/work-list.html', contex)


