from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import login, authenticate
from django.urls import reverse_lazy
from django.views import generic
from django.shortcuts import render, redirect
from praca_inzynierska.models import Actor
from praca_inzynierska.forms import ActorForm

'''
class SignUp(generic.CreateView):
    form_class = UserCreationForm
    success_url = reverse_lazy('login')
    template_name = 'signup.html'
'''

def profile(request):
    return render(request, 'profile.html')

def signup(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        actor_form = ActorForm(request.POST, request.FILES)
        if form.is_valid() and actor_form.is_valid():
            form.save()
            username = form.cleaned_data.get('username')
            raw_password = form.cleaned_data.get('password1')
            user = authenticate(username=username, password=raw_password)
            login(request, user)

            # actor creation
            actor = Actor(user=user)
            actor.save()
            actor.name = actor_form.cleaned_data.get('name')
            actor.surname = actor_form.cleaned_data.get('surname')
            actor.age = actor_form.cleaned_data.get('age')
            actor.sex = actor_form.cleaned_data.get('sex')
            actor.email = actor_form.cleaned_data.get('email')

            if actor.email:
                user.email = actor.email
                user.save()
            actor.city = actor_form.cleaned_data.get('city')
            actor.last_role = actor_form.cleaned_data.get('last_role')
            actor.last_movie = actor_form.cleaned_data.get('last_movie')
            actor.description = actor_form.cleaned_data.get('description')
            actor.visible = actor_form.cleaned_data.get('visible')

            picture = request.FILES.get('profile_picture', None)
            if picture is not None:
                actor.profile_picture = picture

            # categories need separete hangling
            categories_from_form = actor_form.cleaned_data.get('categories')
            for category in categories_from_form:
                actor.categories.add(category)

            actor.save()
            return redirect('/praca_inzynierska/profile/' + str(user.actor.pk))
    else:
        form = UserCreationForm()
        actor_form = ActorForm()
    return render(request, 'signup.html', {'form': form, 'actor_form': actor_form})