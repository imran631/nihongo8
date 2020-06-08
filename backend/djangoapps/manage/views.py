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
        start = int(request.POST.get('start'))
        length = int(request.POST.get('length'))

        level = request.POST.get('level')
        type = request.POST.get('type')
        search_type = request.POST.get('search_type')
        search_text = request.POST.get('search_text')

        order_column = int(request.POST.get('order[0][column]'))
        order_dir = request.POST.get('order[0][dir]')
        order_name = request.POST.getlist('nameList[]')

        if order_dir == 'desc': order_dir = '-'
        else: order_dir = ''

        if level == '': level_list = ['N1', 'N2', 'N3', 'N4', 'N5']
        else: level_list = [level]

        if type == '': type_list = ['N', 'V', 'ADJI', 'ADJN', 'ADV', 'ETC']
        else: type_list = [type]

        kwargs = { '{0}__{1}'.format(search_type, 'contains'): search_text }
        words = Word.objects.filter(level__in=level_list).filter(type__in=type_list).filter(**kwargs).order_by(order_dir + order_name[order_column])

        page = (start + length) / length
        paginator = Paginator(words, length)
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