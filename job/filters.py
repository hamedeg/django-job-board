import django_filters
from .models import Job
class JobFilter(django_filters.FilterSet):
    title = django_filters.CharFilter(lookup_expr='icontains')
    class Meta:
        model = Job
        fields = ['title','job_type','category','experience']
        #exclude = ['owner','description','published_at','image','slug','vacancy']