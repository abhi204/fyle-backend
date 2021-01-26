from bank_app.models import Branch
from bank_app.serializers import BranchSerializer
import django_filters 
from django_filters.rest_framework import FilterSet, DjangoFilterBackend
from rest_framework import filters, generics

# Search across branch field
class BranchAutoCompleteList(generics.ListAPIView):
    queryset = Branch.objects.all().order_by('ifsc')
    serializer_class = BranchSerializer
    filter_backends = [filters.SearchFilter, DjangoFilterBackend]
    search_fields = ['^branch']
    filterset_fields = ['city']

# Search across ALL fields
class AllPossibleMatchList(generics.ListAPIView):
    queryset = Branch.objects.all().order_by('ifsc')
    serializer_class = BranchSerializer
    filter_backends = [filters.SearchFilter, DjangoFilterBackend]
    search_fields = ['^ifsc', '^branch', '^address', '^city', '^district', '^state']
    filterset_fields = ['city']

