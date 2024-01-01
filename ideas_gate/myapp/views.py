
# Create your views here.
from .models import Job
from django.shortcuts import render, redirect, get_object_or_404
from .models import Job
from .forms import JobForm
import django_tables2 as tables
from .tables import JobTable






def dashboard(request):
    # Retrieve all existing job pages
    jobs = Job.objects.all()
    table = JobTable(jobs)
    return render(request, 'myapp/dashboard.html', {'jobs': jobs, 'table': table})



# def add_page(request):
#     if request.method == 'POST':
#         form = PageForm(request.POST)
#         if form.is_valid():
#             page = form.save()
#             return redirect('dashboard')
#     else:
#         form = PageForm()

#     return render(request, 'myapp/add_job.html', {'form': form})



def add_job(request):
    if request.method == 'POST':
        form = JobForm(request.POST,  request.FILES)
        if form.is_valid():
            form.save()
            return redirect('dashboard')
    else:
        form = JobForm() 
    return render(request, 'myapp/add_job.html', {'form': form})

def edit_job(request, job_id):
    job = get_object_or_404(Job, pk=job_id)

    if request.method == 'POST':
        form = JobForm(request.POST, request.FILES, instance=job)
        if form.is_valid():
            form.save()
            return redirect('dashboard')
    else:
        form = JobForm(instance=job)

    return render(request, 'myapp/add_job.html', {'form': form, 'job': job})

def delete_job(request, pk):
    job = get_object_or_404(Job, pk=pk)
    job.delete()
    return redirect('dashboard')

def page_detail(request, pk):
    # Get the job object using get_object_or_404
    job = get_object_or_404(Job, pk=pk)

    # Render the job details using a template
    return render(request, 'myapp/index.html', {'job': job})


# views.py

# def new_page(request, pk):
#     new_page = get_object_or_404(NewPage, pk=pk)
#     return render(request, 'myapp/index.html', {'new_page': new_page})
