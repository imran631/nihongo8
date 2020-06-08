import logging

from django.db import transaction
from django.http import JsonResponse
from django.shortcuts import render
from django.views import View

from backend.djangoapps.manage.mixin import DatatablesMixin
from backend.djangoapps.manage.forms import WordForm, QuizForm, ProblemForm


logger = logging.getLogger(__name__)


class WordView(View, DatatablesMixin):

    template_name = 'backend/manage/word/list.html'

    def get(self, request, *args, **kwargs):
        form = WordForm()
        return render(request, self.template_name, {'form': form})

    def post(self, request, *args, **kwargs):
        words, draw, data = super().paging(request)
        return JsonResponse({
            "recordsTotal": len(words),
            "recordsFiltered": len(words),
            "draw": draw,
            "data": data
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