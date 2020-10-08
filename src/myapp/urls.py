from django.urls import path
from myapp import views
app_name="myapp"

urlpatterns=[
path('',views.ContactView,name="contact"),
path('feedback/',views.FeedbackView,name="feedback")
]
