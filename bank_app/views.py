from bank_app.models import Branch
from bank_app.serializers import BranchSerializer
import django_filters 
from django_filters.rest_framework import FilterSet, DjangoFilterBackend
from rest_framework import filters, generics


class AutoCompleteList(generics.ListAPIView):
    queryset = Branch.objects.all().order_by('ifsc')
    serializer_class = BranchSerializer
    filter_backends = [filters.SearchFilter]
    search_fields = ['^branch']

class AllPossibleMatchList(generics.ListAPIView):
    queryset = Branch.objects.all().order_by('ifsc')
    serializer_class = BranchSerializer
    filter_backends = [filters.SearchFilter]
    search_fields = ['^ifsc', '^branch', '^address', '^city', '^district', '^state']

class BranchFilter(FilterSet):
    ifsc = django_filters.CharFilter(lookup_expr='istartswith')
    branch = django_filters.CharFilter(lookup_expr='istartswith')
    address = django_filters.CharFilter(lookup_expr='istartswith')
    city = django_filters.CharFilter(lookup_expr='istartswith')
    district = django_filters.CharFilter(lookup_expr='istartswith')
    state = django_filters.CharFilter(lookup_expr='istartswith')
    class Meta:
        model = Branch
        fields = ['ifsc', 'branch', 'address', 'city', 'district', 'state']

class SearchByFieldMatchList(generics.ListAPIView):
    queryset = Branch.objects.all().order_by('ifsc')
    serializer_class = BranchSerializer
    filter_backends = [DjangoFilterBackend]
    filterset_class = BranchFilter
