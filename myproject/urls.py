from django.contrib import admin
from django.urls import path
from home import views
from django.conf import settings
from django.conf.urls.static import static


urlpatterns = [
    path('wordtopdf/', views.wordtopdf, name='wordtopdf'),
    path('admin/', admin.site.urls),
    path('convert/', views.pdftoword, name='convert'),
    path('', views.convert_form, name='convert_form'),
    path('download/<str:pk>/', views.downloadpage, name='download'),
]
if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

