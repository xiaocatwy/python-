from django.conf.urls import url
from App import views
urlpatterns = [
    url(r"^$", views.index, name="index"),
    url(r"^echo/$", views.echo, name="echo"),
    # url(r'^start/', views.start, name="start")
]