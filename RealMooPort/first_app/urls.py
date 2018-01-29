from django.conf.urls import url
from first_app import views

app_name = 'first_app'

urlpatterns = [
    url(r'^1_Online_portfolio/$',views.home,name='home'),
    url(r'^2_Certification/$',views.cert,name='cert'),
    url(r'^CGame/$',views.c4game,name='c4game'),
    url(r'^lightQuiz$',views.lightQuiz,name='lightQuiz'),
]
