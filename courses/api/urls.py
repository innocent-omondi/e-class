from django.urls import path, include
from .views import CourseListView, TopicListView, CourseCreateAPIView, TopicCreateAPIView
#, OrderCreateAPIView, OrderDetailAPIView, ProductUpdateAPIView

urlpatterns = [
    path('course-list/', CourseListView.as_view(), name="course-list"),
    path('topic-list/', TopicListView.as_view(), name="topic-list"),
    path('course-create/', CourseCreateAPIView.as_view(), name="course-list"),
    path('topic-create/', TopicCreateAPIView.as_view(), name="topic-list"),
]
