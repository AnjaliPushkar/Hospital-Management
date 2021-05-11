from django.contrib import admin
from django.urls import path
from .import views
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path("", views.doctor, name = "doctor"),
    path("add/", views.add, name="add"),
    path("check/", views.check, name="check"),
    # path('<int:table_id>', views.detail, name='detail'),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
