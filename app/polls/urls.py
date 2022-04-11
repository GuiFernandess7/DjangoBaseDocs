from django.urls import path, re_path
from django.conf.urls.static import static
from django.conf import settings
from django.views.static import serve
from django.contrib.staticfiles.urls import staticfiles_urlpatterns
from . import views

urlpatterns = [
    path('', views.IndexView.as_view(), name='index'),
    path("<int:pk>/", views.DetailView.as_view(), name="detail"),
    path("<int:pk>/results", views.ResultsView.as_view(), name="results"),
    path("<int:pk>/vote", views.vote, name="vote"),
    re_path(r'^static/(?P<path>.*)$', serve,
        {'document_root': settings.STATIC_ROOT})
]

if settings.DEBUG:
    urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
    urlpatterns += staticfiles_urlpatterns()
