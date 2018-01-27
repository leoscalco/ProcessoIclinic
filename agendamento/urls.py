from django.conf.urls import url
from agendamento import views
from rest_framework.urlpatterns import format_suffix_patterns


urlpatterns = [
    url(r'^agendamentos/$', views.AgendamentoList.as_view()),
    url(r'^agendamentos/(?P<pk>[0-9]+)/$', views.AgendamentoDetail.as_view()),
]

urlpatterns = format_suffix_patterns(urlpatterns)