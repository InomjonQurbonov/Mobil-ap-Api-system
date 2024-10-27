from django.db import models

PARTS_CHOICES = [
    ('part_one', 'Part One'),
    ('part_two', 'Part Two'),
    ('part_three', 'Part Three'),
]


class IeltsTest(models.Model):
    part_number = models.CharField(max_length=20, choices=PARTS_CHOICES)
    topic_name = models.CharField(max_length=200, null=True, blank=True)

    def __str__(self):
        return f'{self.part_number} - {self.topic_name}'

    class Meta:
        db_table = 'ielts_test'
        verbose_name = 'Ielts Test'
        verbose_name_plural = 'Ielts Tests'


class IeltsQuestions(models.Model):
    test = models.ForeignKey(IeltsTest, on_delete=models.CASCADE, blank=True, null=True)
    questions = models.CharField(max_length=500, null=True, blank=True)

    def __str__(self):
        return f'{self.test} - {self.questions}'

    class Meta:
        db_table = 'questions'
        verbose_name = 'Questions'
        verbose_name_plural = "Questions"


class IeltsAnswersTest(models.Model):
    questions = models.ForeignKey(IeltsQuestions, on_delete=models.CASCADE, null=True, blank=True)
    answers = models.TextField(null=True, blank=True)

    def __str__(self):
        return f'Answers for {self.questions}'

    class Meta:
        db_table = 'ielts_answers_test'
        verbose_name = 'Ielts Answers Test'
        verbose_name_plural = 'Ielts Answers Tests'
