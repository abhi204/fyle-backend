from django.urls import path
from bank_app.views import AutoCompleteList, AllPossibleMatchList, SearchByFieldMatchList

urlpatterns = [
    path('branches', AllPossibleMatchList.as_view()),
    path('branches/autocomplete', AutoCompleteList.as_view()),
    path('branches/fieldsearch', SearchByFieldMatchList.as_view()),
]
