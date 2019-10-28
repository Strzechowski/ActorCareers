import django_filters
from .models import Actor, Company, Job

class ActorFilter(django_filters.FilterSet):

    class Meta:
        model = Actor
        fields = {
            "name": ['icontains'],
            "surname": ['icontains'],
            "age": ['lte', 'gte'],
            "sex": ['exact'],
            "categories": ['exact'],
        }

ActorFilter.base_filters['age__lte'].label = 'Maximum age'
ActorFilter.base_filters['age__gte'].label = 'Minimum age'
ActorFilter.base_filters['name__icontains'].label = 'Name'
ActorFilter.base_filters['surname__icontains'].label = 'Surname'


class CompanyFilter(django_filters.FilterSet):

    class Meta:
        model = Company
        fields = {
            "name": ['icontains'],
        }


class JobFilter(django_filters.FilterSet):

    class Meta:
        model = Job
        fields = {
            "name": ['icontains'],
            "pay_monthly": ['lte', 'gte'],
            "localization": ['icontains'],
            "categories": ['exact'],
        }

JobFilter.base_filters['pay_monthly__lte'].label = 'Maximum pay monthly'
JobFilter.base_filters['pay_monthly__gte'].label = 'Minimum pay monthly'
JobFilter.base_filters['name__icontains'].label = 'Name'
JobFilter.base_filters['localization__icontains'].label = 'Localization'