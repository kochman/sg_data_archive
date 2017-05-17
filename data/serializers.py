from rest_framework import serializers

from data.models import Body, Meeting, Membership, Motion, Person, Session


class BodySerializer(serializers.ModelSerializer):
    class Meta:
        model = Body
        fields = ('id', 'name', 'created', 'modified')


class MeetingSerializer(serializers.ModelSerializer):
    class Meta:
        model = Meeting
        fields = ('id', 'session', 'date', 'created', 'modified')


class MembershipSerializer(serializers.ModelSerializer):
    class Meta:
        model = Membership
        fields = ('id', 'person', 'session', 'position')


class MotionSerializer(serializers.ModelSerializer):
    class Meta:
        model = Motion
        fields = ('id', 'descriptor', 'text', 'votes_for', 'votes_against', 'abstentions', 'created', 'modified', 'number')


class PersonSerializer(serializers.ModelSerializer):
    memberships = MembershipSerializer(many=True)
    class Meta:
        model = Person
        fields = ('id', 'first_name', 'last_name', 'preferred_name', 'moved_motions', 'seconded_motions', 'memberships')

class SessionSerializer(serializers.ModelSerializer):
    memberships = MembershipSerializer(many=True)
    class Meta:
        model = Session
        fields = ('id', 'body', 'name', 'start_date', 'end_date', 'meetings', 'memberships')

