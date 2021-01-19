from django.urls import path
from bank_app.views import AutoCompleteList, AllPossibleMatchList

urlpatterns = [
    path('branches', AllPossibleMatchList.as_view()),
    path('branches/autocomplete', AutoCompleteList.as_view()),
]
