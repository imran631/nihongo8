from django.db import models
from django.contrib.auth.models import User
from django.utils.translation import gettext_lazy as _


TYPE_CHOICES = [
    ('N', _('Naming word')),
    ('V', _('Verb')),
    ('ADJI', _('adjective I')),
    ('ADJN', _('adjective N')),
    ('ADV', _('adverb')),
    ('ETC', _('ETC'))
]

LEVEL_CHOICES = [
    ('N1', 'JLPT N1'),
    ('N2', 'JLPT N2'),
    ('N3', 'JLPT N3'),
    ('N4', 'JLPT N4'),
    ('N5', 'JLPT N5'),
    ('ETC', _('ETC'))
]

QUIZ_CHOICES = [
    ('LKR', _('Language - Kanji Read')),
    ('LKF', _('Language - Kanji Find')),
    ('LGR', _('Language - Grammar Rule')),
    ('LRP', _('Language - Replace')),
    ('LUF', _('Language - Useful')),
    ('GE', _('Grammar - Empty')),
    ('GO', _('Grammar - Order')),
    ('GL', _('Grammar - Long')),
    ('RS', _('Reading - Short')),
    ('RM', _('Reading - Medium')),
    ('RL', _('Reading - Long')),
    ('RIU', _('Reading - Integrated understanding')),
    ('ROU', _('Reading - Opinion understanding')),
    ('RIS', _('Reading - Information Search')),
    ('ETC', _('ETC'))
]

JLPT_CHOICES = [
    ('N0', _('no license')),
    ('N5', 'JLPT N5'),
    ('N4', 'JLPT N4'),
    ('N3', 'JLPT N3'),
    ('N2', 'JLPT N2'),
    ('N1', 'JLPT N1')
]

JLPT_SEARCH_CHOICES = LEVEL_CHOICES
JLPT_SEARCH_CHOICES.insert(0, ('', _('ALL')))

TYPE_SEARCH_CHOICES = TYPE_CHOICES
TYPE_SEARCH_CHOICES.insert(0, ('', _('ALL')))

QUIZ_SEARCH_CHOICES = QUIZ_CHOICES
QUIZ_SEARCH_CHOICES.insert(0, ('', _('ALL')))


class UserProfile(models.Model):

    user = models.OneToOneField(User, unique=True, db_index=True, related_name='profile', on_delete=models.CASCADE)
    jlpt = models.CharField(max_length=6, choices=JLPT_CHOICES, default='N0')
    point = models.IntegerField(default=0)

    class Meta:
        db_table = "auth_user_profile"


class Word(models.Model):

    level = models.CharField(max_length=6, choices=LEVEL_CHOICES, default='ETC')
    type = models.CharField(max_length=6, choices=TYPE_CHOICES, default='ETC')
    kanji = models.CharField(max_length=255, blank=True, null=True)
    hiragana = models.CharField(max_length=255, blank=True, null=True)
    katakana = models.CharField(max_length=255, blank=True, null=True)
    hangul = models.CharField(max_length=255, blank=True, null=True)
    user = models.ForeignKey(User, on_delete=models.SET_NULL, null=True)
    created_at = models.DateTimeField(blank=True, null=True)
    updated_at = models.DateTimeField(blank=True, null=True)

    class Meta:
        db_table = 'problem_word'


class WordExample(models.Model):

    word = models.ForeignKey(Word, on_delete=models.CASCADE)
    example = models.CharField(max_length=255)
    hangul = models.CharField(max_length=255, blank=True, null=True)
    user = models.ForeignKey(User, on_delete=models.SET_NULL, null=True)
    created_at = models.DateTimeField(blank=True, null=True)
    updated_at = models.DateTimeField(blank=True, null=True)

    class Meta:
        db_table = 'problem_word_example'


class QuizGroup(models.Model):

    level = models.CharField(max_length=6, choices=LEVEL_CHOICES, default='ETC')
    type = models.CharField(max_length=6, choices=QUIZ_CHOICES, default='ETC')
    difficult = models.IntegerField()
    title = models.CharField(max_length=255)
    content = models.CharField(max_length=255)
    user = models.ForeignKey(User, on_delete=models.SET_NULL, null=True)
    created_at = models.DateTimeField(blank=True, null=True)
    updated_at = models.DateTimeField(blank=True, null=True)

    class Meta:
        db_table = 'problem_quiz_group'


class Quiz(models.Model):

    level = models.CharField(max_length=6, choices=LEVEL_CHOICES, default='ETC')
    type = models.CharField(max_length=6, choices=QUIZ_CHOICES, default='ETC')
    quiz = models.CharField(max_length=255, blank=True, null=True)
    hangul = models.CharField(max_length=255, blank=True, null=True)
    user = models.ForeignKey(User, on_delete=models.SET_NULL, null=True)
    created_at = models.DateTimeField(blank=True, null=True)
    updated_at = models.DateTimeField(blank=True, null=True)

    class Meta:
        db_table = 'problem_quiz'


class QuizUnit(models.Model):

    quiz = models.ForeignKey(Quiz, on_delete=models.CASCADE)
    unit = models.CharField(max_length=255, blank=True, null=True)
    hangul = models.CharField(max_length=255, blank=True, null=True)
    right_answer = models.CharField(max_length=255)
    wrong_answer1 = models.CharField(max_length=255)
    wrong_answer2 = models.CharField(max_length=255)
    wrong_answer3 = models.CharField(max_length=255)
    solution = models.CharField(max_length=255, blank=True, null=True)
    point = models.IntegerField(default=0)
    user = models.ForeignKey(User, on_delete=models.SET_NULL, null=True)
    created_at = models.DateTimeField(blank=True, null=True)
    updated_at = models.DateTimeField(blank=True, null=True)

    class Meta:
        db_table = 'problem_quiz_unit'


class QuizGroupLike(models.Model):

    user = models.ForeignKey(User, on_delete=models.CASCADE)
    quiz_group = models.ForeignKey(QuizGroup, on_delete=models.CASCADE)
    created_at = models.DateTimeField(blank=True, null=True)
    updated_at = models.DateTimeField(blank=True, null=True)

    class Meta:
        db_table = 'problem_quiz_group_like'


class QuizGroupWord(models.Model):

    quiz_group = models.ForeignKey(QuizGroup, on_delete=models.CASCADE)
    word = models.ForeignKey(Word, on_delete=models.CASCADE)

    class Meta:
        db_table = 'problem_quiz_group_word'


class QuizGroupQuiz(models.Model):

    quiz_group = models.ForeignKey(QuizGroup, on_delete=models.CASCADE)
    quiz = models.ForeignKey(Quiz, on_delete=models.CASCADE)

    class Meta:
        db_table = 'problem_quiz_group_quiz'


class PointHistory(models.Model):

    user = models.ForeignKey(User, on_delete=models.CASCADE)
    quiz_group = models.ForeignKey(QuizGroup, on_delete=models.SET_NULL, null=True)
    point = models.IntegerField()
    created_at = models.DateTimeField(blank=True, null=True)
    updated_at = models.DateTimeField(blank=True, null=True)

    class Meta:
        db_table = 'problem_point_history'


"""
class TblIndexJlpt(models.Model):
    year = models.CharField(max_length=255)
    round = models.CharField(max_length=255)
    start_date = models.DateTimeField(blank=True, null=True)
    end_date = models.DateTimeField(blank=True, null=True)
    test_date = models.DateTimeField(blank=True, null=True)
    status = models.CharField(max_length=255, blank=True, null=True)

    class Meta:
        db_table = 'tbl_index_jlpt'


class TblNotification(models.Model):
    type = models.CharField(max_length=255)
    title_id = models.IntegerField(blank=True, null=True)
    content = models.CharField(max_length=255, blank=True, null=True)
    user_id = models.IntegerField()
    read_yn = models.CharField(max_length=255, blank=True, null=True)
    read_date = models.DateTimeField(blank=True, null=True)
    regist_id = models.IntegerField(blank=True, null=True)
    regist_date = models.DateTimeField(blank=True, null=True)
    delete_yn = models.CharField(max_length=255, blank=True, null=True)
    delete_date = models.DateTimeField(blank=True, null=True)

    class Meta:
        db_table = 'tbl_notification'


class TblReReply(models.Model):
    reply_id = models.IntegerField()
    content = models.CharField(max_length=255)
    user_id = models.IntegerField()
    regist_date = models.DateTimeField(blank=True, null=True)
    modify_id = models.IntegerField(blank=True, null=True)
    modify_date = models.DateTimeField(blank=True, null=True)
    delete_yn = models.CharField(max_length=255, blank=True, null=True)
    delete_id = models.IntegerField(blank=True, null=True)
    delete_date = models.DateTimeField(blank=True, null=True)

    class Meta:
        db_table = 'tbl_re_reply'


class TblReply(models.Model):
    comm_id = models.IntegerField()
    content = models.CharField(max_length=255)
    user_id = models.IntegerField()
    regist_date = models.DateTimeField(blank=True, null=True)
    modify_id = models.IntegerField(blank=True, null=True)
    modify_date = models.DateTimeField(blank=True, null=True)
    delete_yn = models.CharField(max_length=255, blank=True, null=True)
    delete_id = models.IntegerField(blank=True, null=True)
    delete_date = models.DateTimeField(blank=True, null=True)

    class Meta:
        db_table = 'tbl_reply'


class TblReport(models.Model):
    comm_id = models.IntegerField()
    type = models.CharField(max_length=255)
    reason = models.CharField(max_length=255)
    user_id = models.IntegerField()
    regist_date = models.DateTimeField(blank=True, null=True)
    delete_yn = models.CharField(max_length=255, blank=True, null=True)
    delete_date = models.DateTimeField(blank=True, null=True)
    delete_id = models.IntegerField(blank=True, null=True)

    class Meta:
        db_table = 'tbl_report'


class TblUserJlpt(models.Model):
    user_id = models.IntegerField(primary_key=True)
    pub_jlpt_n1 = models.IntegerField(blank=True, null=True)
    pub_jlpt_n2 = models.IntegerField(blank=True, null=True)
    pub_jlpt_n3 = models.IntegerField(blank=True, null=True)
    pub_jlpt_n4 = models.IntegerField(blank=True, null=True)
    pub_jlpt_n5 = models.IntegerField(blank=True, null=True)
    n1_update_date = models.DateTimeField(blank=True, null=True)
    n2_update_date = models.DateTimeField(blank=True, null=True)
    n3_update_date = models.DateTimeField(blank=True, null=True)
    n4_update_date = models.DateTimeField(blank=True, null=True)
    n5_update_date = models.DateTimeField(blank=True, null=True)

    class Meta:
        db_table = 'tbl_user_jlpt'
"""