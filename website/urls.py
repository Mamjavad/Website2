from django.urls import path
from website.views import *

urlpatterns = [
    path('',index_views),
    path('About',About_views),
    path('contact',contact_views)

]
