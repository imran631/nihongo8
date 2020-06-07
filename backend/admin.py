from django.contrib import admin
from backend.models import Word, WordExample
from backend.models import QuizGroup, Quiz, QuizUnit, QuizGroupLike, QuizGroupWord, QuizGroupQuiz
from backend.models import PointHistory


@admin.register(Word)
class WordAdmin(admin.ModelAdmin):
    list_display = ('id', 'level', 'type', 'kanji', 'hiragana', 'katakana', 'hangul', 'user', 'created_at', 'updated_at')
    list_filter = ('level', 'type')
    search_fields = ['kanji', 'hiragana', 'katakana', 'hangul']


@admin.register(WordExample)
class WordExampleAdmin(admin.ModelAdmin):
    pass


@admin.register(QuizGroup)
class QuizGroupAdmin(admin.ModelAdmin):
    pass


@admin.register(Quiz)
class QuizAdmin(admin.ModelAdmin):
    pass


@admin.register(QuizUnit)
class QuizUnitAdmin(admin.ModelAdmin):
    pass


@admin.register(QuizGroupLike)
class QuizGroupLikeAdmin(admin.ModelAdmin):
    pass


@admin.register(QuizGroupWord)
class QuizGroupWordAdmin(admin.ModelAdmin):
    pass


@admin.register(QuizGroupQuiz)
class QuizGroupQuizAdmin(admin.ModelAdmin):
    pass


@admin.register(PointHistory)
class PointHistoryAdmin(admin.ModelAdmin):
    pass
