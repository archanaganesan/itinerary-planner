from django.conf.urls import url

# current app's views
from . import views

urlpatterns = [
    url(r'^$', views.index, name='ind'),
    # url(r'^/polls/home$', views.home, name='home'),
    url(r'^name$', views.get_name, name='get_name'),
    url(r'^itinerary$', views.get_itinerary, name='get_itinerary'),
]
