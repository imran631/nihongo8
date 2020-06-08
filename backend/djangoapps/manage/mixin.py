from django.core.paginator import Paginator
from backend.models import Word, LEVEL_CHOICES, TYPE_CHOICES

class DatatablesMixin():

    def paging(self, request):
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

        if order_dir == 'desc':
            order_dir = '-'
        else:
            order_dir = ''

        if level == '':
            level_list = [level[0] for level in LEVEL_CHOICES]
        else:
            level_list = [level]

        if type == '':
            type_list = [type[0] for type in TYPE_CHOICES]
        else:
            type_list = [type]

        kwargs = {'{0}__{1}'.format(search_type, 'contains'): search_text}
        words = Word.objects. \
            filter(level__in=level_list). \
            filter(type__in=type_list). \
            filter(**kwargs). \
            order_by(order_dir + order_name[order_column])

        page = (start + length) / length
        paginator = Paginator(words, length)
        page_data = paginator.get_page(page)
        data = []
        for d in page_data:
            tmp = d.__dict__
            del (tmp['_state'])
            data.append(tmp)

        return words, draw, data
