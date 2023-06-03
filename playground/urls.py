from django.urls import path
from . import views

# URLConf module: a Python module that defines a variable named urlpatterns
# that is a list of URL paths to be matched.
urlpatterns = [
    path('hello/', views.hello),
    path('wakeup/', views.wakeup),
    path('teapot/', views.teapot),
    path('lovelyday/', views.lovelyday),
    path('plate_of_tem/', views.plate_of_tem),

]
