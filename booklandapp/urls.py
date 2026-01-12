from django.urls import path
from .views import (
    api_home,
    api_testimonials,
    api_leadership,
    api_gallery,
    api_fees,
    api_events,
    api_featured_events,
    api_alumni,
    api_admission_deadlines,
    api_admissions,
    api_contact,
)

urlpatterns = [
    path("", api_home, name="api_home"),
    path("testimonials/", api_testimonials, name="api_testimonials"),
    path("events/", api_events, name="api_events"),
    path("leadership/", api_leadership, name="api_leadership"),
    path("gallery/", api_gallery, name="api_gallery"),
    path("fees/", api_fees, name="api_fees"),
    path("featured-events/", api_featured_events, name="api_featured_events"),
    path("alumni/", api_alumni, name="api_alumni"),
    path("admission-deadlines/", api_admission_deadlines, name="api_admission_deadlines"),
    path("admissions/submit/", api_admissions, name="api_admissions"),
    path("contact/submit/", api_contact, name="api_contact"),
]
