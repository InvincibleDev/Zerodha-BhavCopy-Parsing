from django.urls import path, include
from api.views import *

urlpatterns = [
    path("", getHeadScrips),
    path("search/<str:scrip_name>/",searchScrip)
]
