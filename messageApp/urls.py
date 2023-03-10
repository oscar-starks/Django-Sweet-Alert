from django.urls import path
from messageApp.views import indexView

urlpatterns = [
    path("", indexView, name = "index")
]
