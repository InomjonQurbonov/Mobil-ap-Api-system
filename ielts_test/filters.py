from django_filters import rest_framework as filters
from ielts_test.models import IeltsTest, IeltsQuestions, IeltsAnswersTest


class IeltsTestFilter(filters.FilterSet):
    class Meta:
        model = IeltsTest
        fields = ['part_number', 'topic_name']