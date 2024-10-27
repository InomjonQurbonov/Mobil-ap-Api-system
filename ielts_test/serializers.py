from rest_framework import serializers
from ielts_test.models import IeltsTest, IeltsAnswersTest, IeltsQuestions


class IeltsTestSerializer(serializers.ModelSerializer):
    class Meta:
        model = IeltsTest
        fields = '__all__'


class GetIeltsTestSerializer(serializers.ModelSerializer):
    class Meta:
        model = IeltsTest
        fields = ['id', 'part_number', 'topic_name']


class IeltsQuestionsSerializers(serializers.ModelSerializer):
    class Meta:
        model = IeltsQuestions
        fields = '__all__'


class GetIeltsQuestionsSerializers(serializers.ModelSerializer):
    class Meta:
        model = IeltsQuestions
        fields = ['id', 'test', 'questions']


class IeltsAnswersTestSerializer(serializers.ModelSerializer):
    class Meta:
        model = IeltsAnswersTest
        fields = '__all__'


class GetIeltsAnswersTestSerializer(serializers.ModelSerializer):
    class Meta:
        model = IeltsAnswersTest
        fields = ['id', 'questions', 'answers']
