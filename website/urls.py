from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name = 'index'),
    path('at-a-glance/', views.at_a_glance, name = 'at-a-glance'),
    path('how-it-works/', views.how_it_works, name = 'how-it-works'),
    path('features/', views.features, name = 'features'),
    path('support/', views.support, name = 'support'),
    path('contact-us/', views.contact_us, name = 'contact-us'),
    path('faq/', views.faq, name = 'faq'),
    path('get-started/', views.get_started, name = 'get-started'),
    
]
