from django.shortcuts import render
from rest_framework import viewsets

from data.models import Body, Meeting, Membership, Motion, Person, Session
from data.serializers import BodySerializer, MeetingSerializer, MembershipSerializer, MotionSerializer, PersonSerializer, SessionSerializer


class BodyViewSet(viewsets.ModelViewSet):
    queryset = Body.objects.all()
    serializer_class = BodySerializer


class MeetingViewSet(viewsets.ModelViewSet):
    queryset = Meeting.objects.all()
    serializer_class = MeetingSerializer


class MembershipViewSet(viewsets.ModelViewSet):
    queryset = Membership.objects.all()
    serializer_class = MembershipSerializer


class MotionViewSet(viewsets.ModelViewSet):
    queryset = Motion.objects.all()
    serializer_class = MotionSerializer


class PersonViewSet(viewsets.ModelViewSet):
    queryset = Person.objects.all()
    serializer_class = PersonSerializer


class SessionViewSet(viewsets.ModelViewSet):
    queryset = Session.objects.all()
    serializer_class = SessionSerializer

