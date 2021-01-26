from django.urls import path
from bank_app.views import BranchAutoCompleteList, AllPossibleMatchList

urlpatterns = [
    path('branches', AllPossibleMatchList.as_view()),
    path('branches/autocomplete', BranchAutoCompleteList.as_view()),
]
