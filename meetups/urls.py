from django.urls import path
from . import views
from .views import Meetup_details

urlpatterns = [
    path('meetups/',views.index,name="all-meetups"),
    path('meetups/success',views.confirm_registeration,name="confirm-registeration"),
    path('meetups/<slug:meetup_slug>/',Meetup_details.as_view(),name="meetup-details")
]