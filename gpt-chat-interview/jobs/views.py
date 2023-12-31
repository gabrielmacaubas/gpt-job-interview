from django.shortcuts import render

from .models import Job


def list_jobs(request):
    return render(
        request, 
        "jobs/list.html", 
        {
            "page_title": "Lista de Vagas", 
            "jobs": Job.objects.all()
        }
    )
