from .views import *
from django.urls import path

urlpatterns = [
    path("", home, name="home"),
    path("about", about, name="about"),
    path("programs", programs, name="programs"),
    path("contactus", contactus, name="contactus"),
    path("addmarks", addmarks, name="addmarks"),
    path("addsubjectmarks", addsubjectmarks, name="addsubjectmarks"),
    path("viewresult", viewresult, name="viewresult"),
    path("signup", signup, name="signup"),
    # path("login", login, name="login"),
]