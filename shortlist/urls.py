from django.urls import path
from shortlist import views
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('', views.upload, name='upload'),
    path('shortlist/', views.shortlist, name='shortlist'),
    path('shortlist/result/', views.result, name='ressult'),
    path("register/", views.register_request, name="register"),
    path("login/", views.login_request, name="login"),
]
if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)