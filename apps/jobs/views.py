from django.shortcuts import render


def jobs(request):
    ctx = {

    }
    return render(request, 'jobs/borwse_job.html', ctx)


def job_detail(request, slug):
    ctx = {

    }
    return render(request, 'jobs/job_details.html', ctx)
