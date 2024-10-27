from django.contrib import admin
from ielts_test.models import IeltsTest, IeltsAnswersTest, IeltsQuestions


class IeltsTestAdmin(admin.ModelAdmin):
    list_display = ('id', 'part_number', 'topic_name')
    search_fields = ('part_number', 'topic_name')
    list_filter = ('part_number', 'topic_name')


class IeltsQuestionsAdmin(admin.ModelAdmin):
    list_display = ('id', 'test', 'questions')
    search_fields = ('test', 'questions')
    list_filter = ('test',)


class IeltsAnswersTestAdmin(admin.ModelAdmin):
    list_display = ('id', 'questions')
    search_fields = ('questions', 'answers')
    list_filter = ('questions',)


admin.site.register(IeltsTest, IeltsTestAdmin)
admin.site.register(IeltsAnswersTest, IeltsAnswersTestAdmin)
admin.site.register(IeltsQuestions, IeltsQuestionsAdmin)
