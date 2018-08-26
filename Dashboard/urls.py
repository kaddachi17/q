from django.conf.urls import url
from . import views

from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    url(r'^$', views.dashboard, name="my_dashboard"),
    url(r'^createyard$', views.affectexam, name="createyard"),
    url(r'^add/(?P<user_id>\d+)$', views.addstudent),
    url(r'^remove/(?P<user_id>\d+)$', views.removestudent),

]
if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
