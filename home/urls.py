from django.urls import path
from . import views

app_name= 'home'

urlpatterns = [
    
    path("", views.industry_summary_list, name="filter"),
    path("likelihood/", views.likelihood, name="likelihood"),
    path("intensity/", views.intensity, name="intensity"),
    path("relevance/", views.relevance, name="relevance"),

    # path("", views.parse_data, name="parse_data"),
    # path("industry_summary_list/", views.industry_summary_list, name="filter"),
]
