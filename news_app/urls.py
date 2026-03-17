from django.urls import path

from news_app.views import news_list_view, news_detail_view, contact_view, texno_news_view

urlpatterns = [
    path('',news_list_view, name='home_page'),
    path('texnologiya/',texno_news_view, name='texno_news'),
    path('<int:id>/', news_detail_view, name='detail_page'),
    path('contact-us/', contact_view, name='contact_page'),

]
