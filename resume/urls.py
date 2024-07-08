from django.conf import settings
from django.conf.urls.static import static
from django.urls import path

from resume.views import index
from .views import contact_view

urlpatterns = [
 path("", index),
 path('contact/', contact_view, name='contact'),
 # path("/com", components),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
