from django.urls import path
from . import views

urlpatterns = [
    path('', views.Reviews.as_view()),
    path('user/<int:user_id>', views.ReviewByUser.as_view()),
    path('feed/<int:feed_id>', views.ReviewByFeed.as_view()),
    path('<int:review_id>', views.ReviewDetail.as_view()),
]