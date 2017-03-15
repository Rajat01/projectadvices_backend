from rest_framework import serializers
from models import Questions, Advices
from django.contrib.auth.models import User


class QuestionSerializer(serializers.ModelSerializer):
    question_id = serializers.IntegerField(source='id', required=False)
    is_anonymously_asked = serializers.BooleanField(required=True)

    class Meta:
        model = Questions
        fields = ('question_id', 'created', 'question', 'asked_by', 'upvote_by', 'is_anonymously_asked')

class QuestionVoteSerializer(serializers.ModelSerializer):
    question_id = serializers.IntegerField(source='id', required=True)

    class Meta:
        model = Questions
        fields = ('question_id', 'question', 'asked_by', 'upvote_by', 'is_anonymously_asked')



class AdviceSerializer(serializers.ModelSerializer):
    question_id = serializers.PrimaryKeyRelatedField(queryset=Questions.objects.all(), required=True, source='question')
    advice_id = serializers.IntegerField(source='id', required=False)

    class Meta:
        model = Advices
        fields = ('advice_id', 'advice_content', 'question_id', 'advised_by', 'upvote_by', 'downvote_by')


class AdviceVoteSerializer(serializers.ModelSerializer):
    question_id = serializers.PrimaryKeyRelatedField(queryset=Questions.objects.all(), required=False,
                                                     source='question')
    advice_id = serializers.IntegerField(source='id', required=False)

    class Meta:
        model = Advices
        fields = ('advice_id', 'upvote_by', 'downvote_by', 'question_id')


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ('id', 'first_name')


# class QuesUserSerializer(serializers.ModelSerializer):
#     question_user = serializers.PrimaryKeyRelatedField(many=True, queryset=Questions.objects.all())
#
#     class Meta:
#         model = User
#         fields = ('id', 'username', 'question_user')
#
#
# class AdvUserSerializer(serializers.ModelSerializer):
#     advice_user = serializers.PrimaryKeyRelatedField(many=True, queryset=Advices.objects.all())
#
#     class Meta:
#         model = User
#         fields = ('id', 'username', 'advice_user')
