from django.db import models


class Player(models.Model):
    name = models.CharField("Имя", max_length=64)
    result = models.IntegerField("Результат", default=0)
    comment = models.CharField("Комментарий", max_length=128, blank=True, default=" ")

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = "Игрок"
        verbose_name_plural = "Игроки"


class Question(models.Model):
    """Вопросы и ответы викторины"""
    id = models.PositiveSmallIntegerField(primary_key=True)
    title = models.TextField()
    answer1 = models.CharField(max_length=64)
    answer2 = models.CharField(max_length=64)
    answer3 = models.CharField(max_length=64)
    answer4 = models.CharField(max_length=64)
    try_answer = models.CharField(max_length=64, default="Answer")

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = "Вопрос"
        verbose_name_plural = "Вопросы"
