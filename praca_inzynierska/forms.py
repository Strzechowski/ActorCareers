from django import forms

from .models import Photo, Actor, Category, Company, Job

class PhotoForm(forms.ModelForm):
    class Meta:
        model = Photo
        fields = ('photo', )

class ActorForm(forms.ModelForm):

    categories = forms.ModelMultipleChoiceField(queryset=Category.objects.all())

    class Meta:
        model = Actor
        fields = ('name', 'surname', 'email', 'city', 'last_role', 'last_movie', 'age', 'sex', 'description', 'profile_picture', 'visible')
        labels = {
            'visible': 'Do you want your profile to be public?'
        }

class CompanyForm(forms.ModelForm):
    class Meta:
        model = Company
        fields = ('name', 'description', 'logo')


class JobForm(forms.ModelForm):

    categories = forms.ModelMultipleChoiceField(queryset=Category.objects.all())

    class Meta:
        model = Job
        fields = ('name', 'pay_monthly', 'description', 'localization', 'picture')