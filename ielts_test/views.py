# views.py
from rest_framework.viewsets import ModelViewSet
from rest_framework.decorators import action
from rest_framework.response import Response
from django.shortcuts import get_object_or_404
from ielts_test.models import IeltsTest, IeltsAnswersTest, IeltsQuestions
from ielts_test import serializers


class IeltsTestViewSet(ModelViewSet):
    queryset = IeltsTest.objects.all()

    def get_serializer_class(self):
        if self.request.method == 'POST':
            return serializers.IeltsTestSerializer
        return serializers.GetIeltsTestSerializer

    @action(detail=False, methods=['get'], url_path=r'part/(?P<part_number>[^/.]+)')
    def filter_by_part(self, request, part_number=None):
        tests = IeltsTest.objects.filter(part_number=part_number)
        serializer = self.get_serializer(tests, many=True)
        return Response(serializer.data)

    @action(detail=False, methods=['get'], url_path=r'part/(?P<part_number>[^/.]+)/(?P<topic_name>[^/.]+)')
    def filter_by_topic(self, request, part_number=None, topic_name=None):
        test = get_object_or_404(IeltsTest, part_number=part_number, topic_name=topic_name)
        questions = IeltsQuestions.objects.filter(test=test)
        serializer = serializers.GetIeltsQuestionsSerializers(questions, many=True)
        return Response(serializer.data)

    @action(detail=False, methods=['get'], url_path=r'part/(?P<part_number>[^/.]+)/(?P<topic_name>[^/.]+)/(?P<question_text>[^/.]+)')
    def filter_by_question(self, request, part_number=None, topic_name=None, question_text=None):
        test = get_object_or_404(IeltsTest, part_number=part_number, topic_name=topic_name)
        question = get_object_or_404(IeltsQuestions, test=test, questions=question_text)
        answer = IeltsAnswersTest.objects.filter(questions=question).first()
        if answer:
            serializer = serializers.GetIeltsAnswersTestSerializer(answer)
            return Response(serializer.data)
        else:
            return Response(
                {"detail": f"Javob topilmadi: '{question_text}' ga tegishli javob mavjud emas."},
                status=404
            )


class IeltsQuestionsViewSet(ModelViewSet):
    queryset = IeltsQuestions.objects.all()

    def get_serializer_class(self):
        if self.request.method == 'POST':
            return serializers.IeltsQuestionsSerializers
        return serializers.GetIeltsQuestionsSerializers


class IeltsAnswersTestViewSet(ModelViewSet):
    queryset = IeltsAnswersTest.objects.all()

    def get_serializer_class(self):
        if self.request.method == 'POST':
            return serializers.IeltsAnswersTestSerializer
        return serializers.GetIeltsAnswersTestSerializer
