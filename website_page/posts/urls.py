from xml.dom.minidom import Document
from django.urls import URLPattern, path
from django.conf import settings
from django.conf.urls.static import static
from . import views
urlpatterns=[
    path('<slug:slug>/',views.detail,name='post_detail'),
]+ static(settings.MEDIA_URL,document_root=settings.MEDIA_ROOT)
