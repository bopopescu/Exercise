from django.urls import path
from polls import views

urlpatterns=[
	path('',views.index,name="polls"),
	path('start/',views.start,name="poll_start")
]
