from django.conf.urls import url

import views
__author__ = 'Ujjwal Wahi'

urlpatterns = [
    url(r'^$', views.TutorialView.as_view(), name="tutorial")
]

