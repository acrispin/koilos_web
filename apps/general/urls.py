from django.conf.urls import url

from apps.general.views import StateApiView

urlpatterns = [
    url(r'^state/(?P<resource_id>\d+)[/]?$', StateApiView.as_view(), name='general_state_api_1'),
    url(r'^state[/]?$', StateApiView.as_view(), name='general_state_api_2'),
]