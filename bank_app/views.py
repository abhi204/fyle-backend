from bank_app.models import Branch
from bank_app.serializers import BranchSerializer
from rest_framework import filters, generics


class AutoCompleteList(generics.ListAPIView):
    queryset = Branch.objects.all().order_by('ifsc')
    serializer_class = BranchSerializer
    filter_backends = [filters.SearchFilter, filters.OrderingFilter]
    search_fields = ['^branch']

class AllPossibleMatchList(generics.ListAPIView):
    queryset = Branch.objects.all().order_by('ifsc')
    serializer_class = BranchSerializer
    filter_backends = [filters.SearchFilter, filters.OrderingFilter]
    search_fields = ['^ifsc', '^branch', '^address', '^city', '^district', '^state']
