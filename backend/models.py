from django.db import models
from django.contrib.auth.models import User
from django.utils import timezone


class UserProfile(models.Model):

    JLPT_CHOICES = (
        ('N1', 'JLPT N1'),
        ('N2', 'JLPT N2'),
        ('N3', 'JLPT N3'),
        ('N4', 'JLPT N4'),
        ('N5', 'JLPT N5'),
        ('N0', '자격증 없음')
    )
    user = models.OneToOneField(User, unique=True, db_index=True, related_name='profile', on_delete=models.CASCADE)
    jlpt = models.CharField(max_length=6, choices=JLPT_CHOICES, default='N0')
    point = models.IntegerField(default=0)

    class Meta:
        db_table = "auth_userprofile"

"""
class FileManage(models.Model):
    user = models.OneToOneField(User, unique=True, db_index=True, related_name='profile_img', on_delete=models.CASCADE)
    raw_name = models.CharField(max_length=255)
    enc_name = models.CharField(max_length=255)
    ext = models.CharField(max_length=255)
    size = models.IntegerField()
    save_path = models.CharField(max_length=255)
    create_at = models.DateTimeField(blank=True, null=True, default=timezone.now)
    update_at = models.DateTimeField(blank=True, null=True)

    class Meta:
        db_table = 'file_manage'
"""

"""
class TblCode(models.Model):
    code_type = models.CharField(max_length=255, blank=True, null=True)
    code_col = models.CharField(max_length=255, blank=True, null=True)
    code_code = models.CharField(max_length=255, blank=True, null=True)
    code_name = models.CharField(max_length=255, blank=True, null=True)
    code_desc = models.CharField(max_length=255, blank=True, null=True)
    user_id = models.IntegerField()
    regist_date = models.DateTimeField(blank=True, null=True)
    modify_id = models.IntegerField(blank=True, null=True)
    modify_date = models.DateTimeField(blank=True, null=True)

    class Meta:
        db_table = 'tbl_code'


class TblCommunity(models.Model):
    type = models.CharField(max_length=255)
    sub_type = models.CharField(max_length=255)
    title = models.CharField(max_length=255)
    content = models.CharField(max_length=255)
    view_cnt = models.CharField(max_length=255)
    like_cnt = models.CharField(max_length=255)
    user_id = models.IntegerField()
    regist_date = models.DateTimeField(blank=True, null=True)
    modify_id = models.IntegerField(blank=True, null=True)
    modify_date = models.DateTimeField(blank=True, null=True)
    delete_yn = models.CharField(max_length=255, blank=True, null=True)
    delete_id = models.IntegerField(blank=True, null=True)
    delete_date = models.DateTimeField(blank=True, null=True)

    class Meta:
        db_table = 'tbl_community'


class TblCore(models.Model):
    level = models.IntegerField()
    type = models.CharField(max_length=255)
    kanji = models.CharField(max_length=255)
    hiragana = models.CharField(max_length=255)
    katakana = models.CharField(max_length=255)
    hangul = models.CharField(max_length=255)
    user_id = models.IntegerField()
    regist_date = models.DateTimeField(blank=True, null=True)
    modify_id = models.IntegerField(blank=True, null=True)
    modify_date = models.DateTimeField(blank=True, null=True)

    class Meta:
        db_table = 'tbl_core'


class TblCoreEx(models.Model):
    core_id = models.IntegerField()
    ex_kanji = models.CharField(max_length=255)
    ex_hangul = models.CharField(max_length=255)
    user_id = models.IntegerField()
    regist_date = models.DateTimeField(blank=True, null=True)
    modify_id = models.IntegerField(blank=True, null=True)
    modify_date = models.DateTimeField(blank=True, null=True)

    class Meta:
        db_table = 'tbl_core_ex'


class TblFile(models.Model):
    raw_name = models.CharField(max_length=255)
    enc_name = models.CharField(max_length=255)
    ext = models.CharField(max_length=255)
    raw_size = models.IntegerField()
    enc_size = models.CharField(max_length=255)
    save_path = models.CharField(max_length=255)
    user_id = models.IntegerField()
    regist_date = models.DateTimeField(blank=True, null=True)
    delete_yn = models.CharField(max_length=255, blank=True, null=True)
    delete_date = models.DateTimeField(blank=True, null=True)
    delete_id = models.IntegerField(blank=True, null=True)

    class Meta:
        db_table = 'tbl_file'


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


class TblPointHistory(models.Model):
    user_id = models.IntegerField()
    quiz_id = models.IntegerField()
    point = models.IntegerField()
    regist_date = models.DateTimeField(blank=True, null=True)
    modify_id = models.IntegerField(blank=True, null=True)
    modify_date = models.DateTimeField(blank=True, null=True)
    delete_yn = models.CharField(max_length=255, blank=True, null=True)
    delete_id = models.IntegerField(blank=True, null=True)
    delete_date = models.DateTimeField(blank=True, null=True)

    class Meta:
        db_table = 'tbl_point_history'


class TblProblem(models.Model):
    type = models.CharField(max_length=255)
    level = models.IntegerField()
    difficult = models.IntegerField()
    title = models.CharField(max_length=255)
    content = models.CharField(max_length=255)
    user_id = models.IntegerField()
    regist_date = models.DateTimeField(blank=True, null=True)
    modify_id = models.IntegerField(blank=True, null=True)
    modify_date = models.DateTimeField(blank=True, null=True)
    delete_yn = models.CharField(max_length=255, blank=True, null=True)
    delete_id = models.IntegerField(blank=True, null=True)
    delete_date = models.DateTimeField(blank=True, null=True)

    class Meta:
        db_table = 'tbl_problem'


class TblProblemCore(models.Model):
    problem_id = models.IntegerField()
    core_id = models.IntegerField()

    class Meta:
        db_table = 'tbl_problem_core'


class TblProblemLike(models.Model):
    user_id = models.IntegerField()
    problem_id = models.IntegerField()
    delete_yn = models.CharField(max_length=255, blank=True, null=True)
    delete_date = models.DateTimeField(blank=True, null=True)

    class Meta:
        db_table = 'tbl_problem_like'


class TblProblemQuiz(models.Model):
    problem_id = models.IntegerField()
    quiz_id = models.IntegerField()

    class Meta:
        db_table = 'tbl_problem_quiz'


class TblQuiz(models.Model):
    type = models.CharField(max_length=255)
    level = models.IntegerField()
    quiz = models.CharField(max_length=255)
    quiz_hangule = models.CharField(max_length=255)
    problem1 = models.CharField(max_length=255)
    problem2 = models.CharField(max_length=255)
    problem3 = models.CharField(max_length=255)
    problem4 = models.CharField(max_length=255)
    solve = models.CharField(max_length=255)
    solution = models.CharField(max_length=255, blank=True, null=True)
    point = models.IntegerField()
    user_id = models.IntegerField()
    regist_date = models.DateTimeField(blank=True, null=True)
    modify_id = models.IntegerField(blank=True, null=True)
    modify_date = models.DateTimeField(blank=True, null=True)

    class Meta:
        db_table = 'tbl_quiz'


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