from rest_framework import serializers

from data.models import Body, Meeting, Motion, Person, Session


class BodySerializer(serializers.ModelSerializer):
    class Meta:
        model = Body
        fields = ('id', 'name')


class MeetingSerializer(serializers.ModelSerializer):
    class Meta:
        model = Meeting
        fields = ('id', 'session', 'date')


class MotionSerializer(serializers.ModelSerializer):
    class Meta:
        model = Motion
        fields = ('id', 'descriptor', 'text', 'votes_for', 'votes_against', 'abstentions', 'created', 'modified', 'number')


class PersonSerializer(serializers.ModelSerializer):
    class Meta:
        model = Person
        fields = ('id', 'first_name', 'last_name', 'preferred_name', 'moved_motions', 'seconded_motions')

class SessionSerializer(serializers.ModelSerializer):
    class Meta:
        model = Session
        fields = ('id', 'body', 'name', 'start_date', 'end_date', 'meetings')

