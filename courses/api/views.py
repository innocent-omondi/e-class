from django.http import HttpResponse
from django.conf import settings
#from django.core.mail import send_mail

from courses.models import Course,  Topic
from .serializers import CourseSerializer, TopicSerializer

from rest_framework.response import Response
from rest_framework.permissions import AllowAny
from rest_framework.decorators import api_view
from rest_framework import status
from rest_framework.generics import ListAPIView, CreateAPIView

class CourseListView(ListAPIView):
        permission_classes = ([AllowAny])
        queryset = Course.objects.all()
        serializer_class = CourseSerializer

class TopicListView(ListAPIView):
	queryset = Topic.objects.all()
	serializer_class = TopicSerializer

	
class CourseCreateAPIView(CreateAPIView):
	queryset = Course.objects.all()
	serializer_class = CourseSerializer                

class TopicCreateAPIView(CreateAPIView):
	queryset = Topic.objects.all()
	serializer_class = TopicSerializer


