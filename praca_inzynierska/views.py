from django.shortcuts import render, redirect
from praca_inzynierska.models import Announcement, User
from django.core.files.storage import FileSystemStorage
from .forms import PhotoForm, ActorForm, CompanyForm, JobForm
from .models import Photo, Actor, User, Company, Job
from .filters import ActorFilter, CompanyFilter, JobFilter
from django.templatetags.static import static
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger


def index(request):
    context = {}
    return render(request, "index.html", context)


def about(request):
    context = {}
    return render(request, "about.html", context)


def upload(request):
    if request.method == 'POST':
        form = PhotoForm(request.POST, request.FILES)
        if form.is_valid():
            photo_instance = form.save(commit=False)
            photo_instance.user = request.user
            photo_instance.save()
            return redirect('gallery', pk=request.user.pk)
    else:
        form = PhotoForm()
    return render(request, 'upload.html', {
        'form': form
    })


def delete_photo(request, pk):
    if request.method == 'POST':
        photo = Photo.objects.get(pk=pk)
        photo.delete()
    return redirect('gallery', pk=request.user.pk)


def update_profile(request):
    user = request.user
    initial_form = {
        'name': user.actor.name,
        'surname': user.actor.surname,
        'age': user.actor.age,
        'sex': user.actor.sex,
        'email': user.actor.email,
        'city': user.actor.city,
        'last_role': user.actor.last_role,
        'last_movie': user.actor.last_movie,
        'description': user.actor.description,
        'profile_picture': user.actor.profile_picture,
        'cv': user.actor.cv,
        'visible': user.actor.visible,
        'categories': [ request.user.actor.categories ], #initial category does not work...
    }

    if request.method == 'POST':
        form = ActorForm(request.POST, request.FILES, initial=initial_form)
        if form.is_valid():
            if request.user.actor is None:  #This might be needed to handle user who is editing profile 1st time
                print("aaaa")
                #actor_instance = form.save(commit=False)
            user.actor.name = form.cleaned_data.get('name')
            user.actor.surname = form.cleaned_data.get('surname')
            user.actor.age = form.cleaned_data.get('age')
            user.actor.sex = form.cleaned_data.get('sex')
            user.actor.email = form.cleaned_data.get('email')
            user.email = user.actor.email
            user.actor.city = form.cleaned_data.get('city')
            user.actor.last_role = form.cleaned_data.get('last_role')
            user.actor.last_movie = form.cleaned_data.get('last_movie')
            user.actor.description = form.cleaned_data.get('description')
            user.actor.cv = form.cleaned_data.get('cv')
            user.actor.visible = form.cleaned_data.get('visible')
            picture = request.FILES.get('profile_picture', None)
            if picture is not None:
                user.actor.profile_picture = picture
            user.actor.categories.clear()
            user.actor.save()
            user.save()
            categories_from_form = form.cleaned_data.get('categories')
            for category in categories_from_form:
                user.actor.categories.add(category)

            user.actor.save()
            return redirect('/praca_inzynierska/profile/' + str(user.actor.pk))
    else:
        form = ActorForm(initial=initial_form)
    return render(request, 'update_profile.html', {
        'form': form
    })


def profile(request, pk):
    actor = Actor.objects.get(pk=pk)
    categories = actor.categories.all()
    photos = Photo.objects.filter(user=actor.user)
    context = {
        "actor": actor,
        "categories": categories,
        "photos": photos,
    }
    return render(request, 'profile.html', context)


def announcement_detail(request, pk):
    actor = Actor.objects.get(pk=pk)
    categories = actor.categories.all()
    photos = Photo.objects.filter(user=actor.user)
    context = {
        "actor": actor,
        "categories": categories,
        "photos": photos,
    }
    return render(request, 'announcement_detail.html', context)


def search_announcements(request):
    actors_filter = ActorFilter(request.GET, queryset=Actor.objects.exclude(visible='No'))
    return render(request, 'search_announcements.html', {'filter': actors_filter})


def announcement(request):
    actors_filter = ActorFilter(request.GET, queryset=Actor.objects.exclude(visible='No'))
    return render(request, 'announcement.html', {'filter': actors_filter})


def gallery(request, pk):
    photos = Photo.objects.filter(user=pk)
    return render(request, 'gallery.html', {'photos': photos})


def create_company(request):
    if hasattr(request.user, 'company'):
        return redirect('company_profile', request.user.company.pk)
    elif request.method == 'POST':
        form = CompanyForm(request.POST)
        if form.is_valid():
            company_instance = form.save(commit=False)
            company_instance.user = request.user
            company_instance.save()
            return redirect('company_profile', request.user.company.pk)
    else:
        form = CompanyForm()
    return render(request, 'create_company.html', {
        'form': form
    })


def edit_company(request):
    user = request.user

    initial_form = {
        'name': user.company.name,
        'description': user.company.description,
        'logo': user.company.logo
    }

    if request.method == 'POST':
        form = CompanyForm(request.POST, initial=initial_form)
        if form.is_valid():
            user.company.name = form.cleaned_data.get('name')
            user.company.description = form.cleaned_data.get('description')
            picture = request.FILES.get('logo', None)
            if picture is not None:
                user.company.logo = picture
            user.company.save()
            return redirect('company_profile', user.company.pk)
    else:
        form = CompanyForm(initial=initial_form)
    return render(request, 'create_company.html', {
        'form': form
    })


def companies(request):
    company_filter = CompanyFilter(request.GET, queryset=Company.objects.exclude(name__isnull=True))
    return render(request, 'companies.html', {'filter': company_filter})


def company(request, pk):
    company = Company.objects.get(pk=pk)
    jobs = Job.objects.filter(company=company)
    context = {
        "company": company,
        "jobs": jobs
    }
    return render(request, 'company.html', context)


def company_profile(request, pk):
    company = Company.objects.get(pk=pk)
    jobs = Job.objects.filter(company=company)
    context = {
        "company": company,
        "jobs": jobs
    }
    return render(request, 'company_profile.html', context)


def add_job(request):
    if request.method == 'POST':
        form = JobForm(request.POST, request.FILES)
        if form.is_valid():
            job_instance = form.save(commit=False)
            job_instance.company = request.user.company
            job_instance.save()

            categories_from_form = form.cleaned_data.get('categories')
            for category in categories_from_form:
                job_instance.categories.add(category)
            job_instance.save()

            return redirect('search_jobs')
    else:
        form = JobForm()
    return render(request, 'add_job.html', {
        'form': form
    })


def search_jobs(request):
    jobs_filter = JobFilter(request.GET, queryset=Job.objects.all())
    return render(request, 'search_jobs.html', {'filter': jobs_filter})


def job_offer(request, pk):
    job = Job.objects.get(pk=pk)
    categories = job.categories.all()
    context = {
        'job': job,
        'categories': categories,
    }
    return render(request, 'job_offer.html', context)