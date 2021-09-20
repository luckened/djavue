from core import views
from django.conf.urls import url

urlpatterns = [
    url(r'^api/dapau$', views.dapau),
    url(r'^api/login$', views.login),
    url(r'^api/logout$', views.logout),
    url(r'^api/whoami$', views.whoami),

    url(r'^api/list_tweets$', views.list_tweets),
    url(r'^api/get_user_details$', views.get_user_details),
    url(r'^api/toggle_follow$', views.toggle_follow),
    url(r'^api/tweet$', views.tweet),
]
