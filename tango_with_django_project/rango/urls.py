from django.urls import path
from rango import views
from django.conf import settings
from django.conf.urls.static import static
app_name = 'rango'
urlpatterns = [
    path('index/', views.index, name='index'),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
