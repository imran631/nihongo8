import logging

from django.core.paginator import Paginator
from django.db import transaction
from django.http import JsonResponse
from django.shortcuts import render
from django.views import View

from backend.djangoapps.manage.forms import WordForm, QuizForm, ProblemForm
from backend.models import Word

logger = logging.getLogger(__name__)


class WordView(View):

    template_name = 'backend/manage/word/list.html'

    def get(self, request, *args, **kwargs):
        form = WordForm()
        return render(request, self.template_name, {'form': form})

    def post(self, request, *args, **kwargs):

        draw = request.POST.get('draw')
        start = request.POST.get('start')
        length = request.POST.get('length')

        level = request.POST.get('level')
        if level == '':
            level_list = ['N1', 'N2', 'N3', 'N4', 'N5']
        else:
            level_list = []
            level_list.append(level)

        type = request.POST.get('type')
        if type == '':
            type_list = ['N', 'V', 'ADJI', 'ADJN', 'ADV', 'ETC']
        else:
            type_list = []
            type_list.append(type)

        search_type = request.POST.get('search_type')
        search_text = request.POST.get('search_text')
        if search_type == 'kanji' and search_text != '':
            words = Word.objects.filter(level__in=level_list).filter(type__in=type_list).filter(kanji__contains=search_text)
        elif search_type == 'hiragana' and search_text != '':
            words = Word.objects.filter(level__in=level_list).filter(type__in=type_list).filter(hiragana__contains=search_text)
        elif search_type == 'katakana' and search_text != '':
            words = Word.objects.filter(level__in=level_list).filter(type__in=type_list).filter(katakana__contains=search_text)
        elif search_type == 'hangul' and search_text != '':
            words = Word.objects.filter(level__in=level_list).filter(type__in=type_list).filter(hangul__contains=search_text)
        else:
            words = Word.objects.filter(level__in=level_list).filter(type__in=type_list)

        print('start => ', start)
        print('length => ', length)

        page = (int(start) + int(length)) / int(length)
        paginator = Paginator(words, length)

        print('page => ', page)

        page_data = paginator.get_page(page)
        dt_data = []
        for data in page_data:
            tmp = data.__dict__
            del(tmp['_state'])
            dt_data.append(tmp)
        return JsonResponse({
            "recordsTotal": len(words),
            "recordsFiltered": len(words),
            "draw": draw,
            "data": dt_data
        })


class WordMoidfyView(View):

    template_name = 'backend/manage/word/modify.html'

    def get(self, request, *args, **kwargs):
        form = WordForm()
        return render(request, self.template_name, {'form': form})

    def post(self, request, *args, **kwargs):
        pass


class WordAddView(View):

    template_name = 'backend/manage/word/add.html'

    def get(self, request, *args, **kwargs):
        form = WordForm()
        return render(request, self.template_name, {'form': form})

    def post(self, request, *args, **kwargs):
        pass


class QuizView(View):

    template_name = 'backend/manage/quiz/list.html'

    def get(self, request, *args, **kwargs):
        form = QuizForm()
        return render(request, self.template_name, {'form': form})

    def post(self, request, *args, **kwargs):
        pass


class QuizModifyView(View):

    template_name = 'backend/manage/quiz/modify.html'

    def get(self, request, *args, **kwargs):
        form = WordForm()
        return render(request, self.template_name, {'form': form})

    def post(self, request, *args, **kwargs):
        pass


class QuizAddView(View):

    template_name = 'backend/manage/quiz/add.html'

    def get(self, request, *args, **kwargs):
        form = WordForm()
        return render(request, self.template_name, {'form': form})

    def post(self, request, *args, **kwargs):
        pass


class ProblemView(View):

    template_name = 'backend/manage/problem/list.html'

    def get(self, request, *args, **kwargs):
        form = ProblemForm()
        return render(request, self.template_name, {'form': form})

    def post(self, request, *args, **kwargs):
        pass


class ProblemMoidfyView(View):

    template_name = 'backend/manage/problem/modify.html'

    def get(self, request, *args, **kwargs):
        form = WordForm()
        return render(request, self.template_name, {'form': form})

    def post(self, request, *args, **kwargs):
        pass


class ProblemAddView(View):

    template_name = 'backend/manage/problem/add.html'

    def get(self, request, *args, **kwargs):
        form = WordForm()
        return render(request, self.template_name, {'form': form})

    def post(self, request, *args, **kwargs):
        pass