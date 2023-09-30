from django.urls import path

from . import views

app_name = "polls"
urlpatterns = [
    path("", views.IndexView.as_view(), name="index"),
    path("polls/", views.PollsIndexView.as_view(), name="polls"),
    path("polls/<int:pk>/", views.PollsDetailView.as_view(), name="detail"),
    path("polls/<int:pk>/results/", views.PollsResultsView.as_view(), name="results"),
    path("polls/<int:question_id>/vote/", views.vote, name="vote"),
]
