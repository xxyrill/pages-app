from django.urls import path

# tawagon ni sya to power-up the URL pattern

from .views import HomePageView, AboutPageView #new

# pasabot ani is gna refer nato si views.py as .views ug gina-ingnan nato si
# Django na pangitaon sa current directory ang views.py na file

urlpatterns = [

    path('', HomePageView.as_view(), name='home'),
    path('about', AboutPageView.as_view(), name='about'), # new


]

# l11, pag class based na view, need ka mag add ug as_view() sa tumoy sa view name

# ang main take away aning urls.py is sya mag determine kung asa padulong
# ang content (to where the content is going)