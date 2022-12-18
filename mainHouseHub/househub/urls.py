from django.urls import path
from . import views

# You can think of this as the hub for valid paths of the page, when we define a new fun in views we add it here
app_name = "househub"
urlpatterns = [
    # First var is for the path, second for the related function in views, and name is so that we can reference it by the name in the HTML with built-in python
    path("", views.index, name = "index"),
    path("sign_up/", views.sign_up, name = "sign_up"),
]