from django.conf.urls import url
from . import views
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
                  url(r'^$', views.index, name='index'),
                  url(r'^(?P<exam_id>[0-9]+)/passe/$', views.passe, name='passe_exam'),
                  url(r'^(?P<exam_id>[0-9]+)/mode/$', views.mode, name='mode_exam'),

                  url(r'^(?P<exam_id>[0-9]+)/$', views.detail, name='detail'),
                  url(r'^(?P<exam_id>[0-9]+)/reponse/$', views.reponse, name='reponse'),
                  url(r'^(?P<exam_id>[0-9]+)/edit/$', views.edit, name='edit'),
                  url(r'^(?P<Quest_id>[0-9]+)/editfree/$', views.editfree, name='editfree'),
                  url(r'^(?P<Quest_id>[0-9]+)/editmulti/$', views.editmulti, name='editmulti'),
                  url(r'^(?P<Quest_id>[0-9]+)/editone/$', views.editone, name='editone'),
                  url(r'^create/$', views.create_view, name='create_view'),
                  url(r'^createQuest/$', views.createExam, name='createExam'),
                  url(r'^secondeQuest/$', views.secondeQuest, name='secondeQuest'),
                  url(r'^(?P<exam_id>[0-9]+)/addQuest/$', views.addQuest, name='addQuest'),
                  url(r'^(?P<exam_id>[0-9]+)/deleteEXam/$', views.deleteEXam, name='deleteEXam'),
                  url(r'^(?P<question_id>[0-9]+)/deleteQuest/$', views.deleteQuest, name='deleteQuest'),
                  url(r'^(?P<exam_id>[0-9]+)/edit/$', views.edit, name='edit'),
                  url(r'^(?P<pk>[0-9]+)/assigne_student/$', views.assigne_classroom, name='assigne_classroom'),
                  url(r'^(?P<pk>[0-9]+)/add/(?P<selected_id>[0-9]+)/to_yard/$', views.add_to_yard, name='add_to_yard'),

                  url(r'^(?P<pk>[0-9]+)/addStudent/$', views.addStudent, name='addStudent'),
                  url(r'^(?P<exam_id>[0-9]+)/passe/(?P<Quest_id>[0-9]+)$', views.passeQuest, name='passeQuest'),
                  url(r'^(?P<exam_id>[0-9]+)/result/$', views.result, name='result'),
                  url(r'^sendmail/$', views.sendmail, name='sendemail'),

              ] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
