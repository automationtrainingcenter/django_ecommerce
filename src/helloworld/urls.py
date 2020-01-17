from django.conf.urls import url
from helloworld import views

app_name = 'helloworld'
urlpatterns = [
    url(r'^$', views.home_page, name='home'),
    url(r'^about/$', views.about_page, name='about'),
    url(r'^contact/$', views.contact_page, name='contact'),
    url(r'^login/$', views.login_page, name='login'),
    url(r'^register/$', views.register_page, name='register'),
]
