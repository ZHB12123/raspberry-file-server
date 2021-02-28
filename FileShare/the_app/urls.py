from django.conf.urls import url
from django.conf import settings
from django.conf.urls.static import static
from . import views

app_name = 'demo'

urlpatterns = [
    url(r'index',views.index,name='index'),
    url(r'files',views.files,name='files'),
    url(r'download',views.download,name='download'),
    ]
