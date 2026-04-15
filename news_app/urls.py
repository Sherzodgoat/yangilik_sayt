from django.urls import path

from news_app.views import news_list_view, news_detail_view, contact_view, texno_news_view, NewsUpdateView, \
    NewsDeleteView, NewsCreateView, sport_news_view, uz_news_view, siyosiy_news_view, iqtisodiy_news_view

urlpatterns = [
    path('',news_list_view, name='home_page'),
    path('texnologiya/',texno_news_view, name='texno_news'),
    path('sport/',sport_news_view, name='sport_news'),
    path('uzbekiston/', uz_news_view, name='uz_news' ),
    path('siyosiy/',siyosiy_news_view, name='siyosiy_news'),
    path('iqtisodiy/', iqtisodiy_news_view, name='iqtisoy_news' ),



    path('contact-us/',contact_view, name='contact_page'),
    path('<slug>/update/', NewsUpdateView.as_view(), name='update'),
    path('<slug>/delete/', NewsDeleteView.as_view(), name='delete'),
    path('news/create/', NewsCreateView.as_view(), name='create'),

    path('news/<slug:slug>/', news_detail_view, name='detail_page'),

]
