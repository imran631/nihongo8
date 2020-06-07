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
        words = Word.objects.filter()
        paginator = Paginator(words, 10)
        page_data = paginator.get_page(1)
        dt_data = []
        for data in page_data:
            tmp = data.__dict__
            del(tmp['_state'])
            dt_data.append(tmp)
        return JsonResponse({
            "recordsTotal": len(words),
            "recordsFiltered": len(words),
            "draw": 1,
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